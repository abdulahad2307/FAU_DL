"""Verify the question bank. Run this before deploying.

merge_bank.py validates each question as it is added; this script re-checks the
finished file end to end and reports the quality signals that matter for exam
practice — answer-position bias, duplicate questions, excluded-topic leakage and
the option-length tell.

Exit code is 0 when every hard check passes, 1 otherwise. Soft warnings do not
fail the run; they are printed so you can decide.

    python scripts/verify_bank.py
"""

import itertools
import json
import os
import re
import statistics
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "data", "questions.json")

VALID_DIFF = {"basics", "intermediate", "advanced"}
DIFF_POINTS = {"basics": {1}, "intermediate": {2, 3}, "advanced": {3, 4}}
VALID_SOURCE = {"seed", "lecture notes", "past exams", "exercises", "generated"}
EXCLUDED_KEYWORDS = ["weakly supervised", "known operator", "graph neural network",
                     "graph convolution", "self-supervised", "self supervised"]
KEYS = ["A", "B", "C", "D"]

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def canon(s):
    """Aggressive normalisation, for spotting the same question reworded."""
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())


def soft(s):
    """Light normalisation, for spotting genuinely identical option texts.

    canon() strips punctuation, which collapses distinct maths into the same
    string: '-1' and '1' both become '1', and 'x²' and '-x' both become 'x'.
    Comparing option texts needs case and spacing folded and nothing else.
    """
    return " ".join(str(s).lower().split())


def main():
    data = json.load(open(BANK))
    qs = data["questions"]
    meta = data["meta"]
    n = len(qs)

    print(f"Bank: {n} questions, {sum(q['points'] for q in qs)} points\n")

    # ---------------- hard checks: structure ----------------------------
    ids = [q["id"] for q in qs]
    if len(set(ids)) != n:
        err(f"duplicate ids: {[i for i, c in Counter(ids).items() if c > 1][:5]}")

    for q in qs:
        w = q["id"]
        if q["difficulty"] not in VALID_DIFF:
            err(f"{w}: bad difficulty {q['difficulty']!r}")
        elif q["points"] not in DIFF_POINTS[q["difficulty"]]:
            err(f"{w}: {q['points']}p is invalid for {q['difficulty']}")
        if q.get("source") not in VALID_SOURCE:
            err(f"{w}: bad source {q.get('source')!r}")
        if sorted(q["options"]) != KEYS:
            err(f"{w}: option keys are {sorted(q['options'])}")
        if any(not str(v).strip() for v in q["options"].values()):
            err(f"{w}: has an empty option")
        if len(set(soft(v) for v in q["options"].values())) != 4:
            err(f"{w}: has two identical options")
        if not q.get("explanation", "").strip():
            err(f"{w}: no explanation")
        elif not q["explanation"].rstrip().endswith((".", "!", "?")):
            err(f"{w}: explanation does not end in a full stop")
        for c in q["correct_answers"]:
            if c not in q["options"]:
                err(f"{w}: correct answer {c} is not an option")
        # SS26 rule B: every question has exactly one correct option, and
        # marking more than one scores zero. Multi-select must not appear.
        if q["type"] != "single_choice":
            err(f"{w}: type is {q['type']!r}, but SS26 allows single_choice only")
        if len(q["correct_answers"]) != 1:
            err(f"{w}: has {len(q['correct_answers'])} correct answers, SS26 allows one")
        if "select all" in q["question"].lower():
            err(f"{w}: prompts for multiple answers, which scores zero in SS26")
        if q["source"] == "exercises" and q.get("exercise") not in (0, 1, 2, 3, 4):
            err(f"{w}: exercise question without a valid sheet number")
        if q["topic"] in meta["excluded_topics"]:
            err(f"{w}: filed under excluded topic {q['topic']}")

    # ---------------- hard check: excluded topics -----------------------
    for q in qs:
        blob = (q["question"] + " " + " ".join(q["options"].values()) + " " +
                q["explanation"]).lower()
        for kw in EXCLUDED_KEYWORDS:
            if kw in blob:
                err(f"{q['id']}: needs excluded material ({kw})")

    # ---------------- hard check: duplicates ----------------------------
    texts = Counter(canon(q["question"]) for q in qs)
    for t, c in texts.items():
        if c > 1:
            err(f"duplicate question text x{c}: {t[:60]}")

    for a, b in itertools.combinations(qs, 2):
        oa = {canon(v) for v in a["options"].values()}
        ob = {canon(v) for v in b["options"].values()}
        if len(oa & ob) < 3:
            continue
        ca = {canon(a["options"][c]) for c in a["correct_answers"]}
        cb = {canon(b["options"][c]) for c in b["correct_answers"]}
        if ca == cb:
            err(f"{a['id']} and {b['id']} are the same question reworded")

    # ---------------- soft check: answer position -----------------------
    sc = [q for q in qs if q["type"] == "single_choice"]
    if not sc:
        err("no single_choice questions in the bank")
    pos = Counter(q["correct_answers"][0] for q in sc)
    print("Correct-answer position (single choice):")
    for k in KEYS:
        share = pos[k] / len(sc)
        flag = "  <-- skewed" if abs(share - 0.25) > 0.08 else ""
        print(f"  {k}: {pos[k]:>3} ({share:>5.1%}){flag}")
        if abs(share - 0.25) > 0.08:
            warn(f"answer position {k} is at {share:.1%}; run scripts/rebalance_options.py")

    # ---------------- soft check: option-length tell --------------------
    longest = sum(1 for q in sc
                  if max(q["options"], key=lambda k: len(q["options"][k])) == q["correct_answers"][0])
    share = longest / len(sc)
    gaps = []
    for q in sc:
        c = q["correct_answers"][0]
        others = [len(v) for k, v in q["options"].items() if k != c]
        gaps.append(len(q["options"][c]) - statistics.mean(others))
    print(f"\nCorrect answer is the longest option: {longest}/{len(sc)} ({share:.1%}, chance 25%)")
    print(f"Median length gap over the distractors: {statistics.median(gaps):+.0f} characters")
    if share > 0.40:
        warn(f"the longest option is correct {share:.0%} of the time — a student can "
             f"beat the bank without knowing the material by always picking the "
             f"wordiest answer. Lengthening the distractors is the fix.")

    # ---------------- report --------------------------------------------
    print(f"\nBy source: {dict(Counter(q['source'] for q in qs))}")
    print(f"By difficulty: {dict(Counter(q['difficulty'] for q in qs))}")
    print(f"By type: {dict(Counter(q['type'] for q in qs))}")

    print("\n" + "=" * 62)
    if errors:
        print(f"FAILED — {len(errors)} hard error(s):")
        for e in errors[:40]:
            print("  -", e)
        if len(errors) > 40:
            print(f"  ... and {len(errors) - 40} more")
    else:
        print("PASSED — all hard checks clean.")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print("  !", w)
    print("=" * 62)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
