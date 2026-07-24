"""Merge the seed bank (data/questions.json) with the exam-, lecture- and
exercise-derived question modules, validate everything, re-assign ids, and write
the file back. Safe to re-run: duplicates are detected by question text.

Run scripts/backfill_seed.py first if any question is still missing an
explanation or a source tag.
"""

import json, os, random, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from questions_exams import E
from questions_exams_extra import E2
from questions_exercises import X
from questions_chapters import K
from questions_singleanswer import S

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "data", "questions.json")

VALID_DIFF = {"basics", "intermediate", "advanced"}
DIFF_POINTS = {"basics": {1}, "intermediate": {2, 3}, "advanced": {3, 4}}
VALID_SOURCE = {"seed", "lecture notes", "past exams", "exercises"}

# The course notes exclude these topics, so nothing in the bank may require them.
EXCLUDED_KEYWORDS = [
    "weakly supervised", "known operator", "graph neural network",
    "graph convolution", "self-supervised", "self supervised",
]

def canon(s):
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())


data = json.load(open(BANK))
existing = data["questions"]
seen = {canon(q["question"]) for q in existing}


def words(s):
    return set(w for w in re.sub(r"[^a-z0-9 ]", " ", s.lower()).split() if len(w) > 3)


def near_duplicate(q, pool):
    """Catch rephrased duplicates that an exact-text check misses.

    Boilerplate stems like 'Which statements about X are TRUE? (Select all that
    apply)' overlap heavily by construction, so the options are compared too:
    two questions only count as duplicates when the stems AND the answer texts
    both overlap.
    """
    qa = words(q["question"])
    qo = words(" ".join(q["options"].values()))
    if not qa:
        return None
    for other in pool:
        oa = words(other["question"])
        if not oa:
            continue
        if len(qa & oa) / len(qa | oa) <= 0.6:
            continue
        oo = words(" ".join(other["options"].values()))
        if oo and len(qo & oo) / len(qo | oo) > 0.5:
            return other
    return None


def same_option_set(q, pool):
    """Catch reworded stems that reuse the same options and the same answer.

    'Which of the following is NOT a technique to visualize important image
    areas' and 'Which of these is NOT a technique for visualising important
    image regions' share almost no rare words, so the stem check above misses
    them, but they are plainly the same question.
    """
    opts = {canon(v) for v in q["options"].values()}
    corr = {canon(q["options"][c]) for c in q["correct_answers"]}
    for other in pool:
        oopts = {canon(v) for v in other["options"].values()}
        if len(opts & oopts) < 3:
            continue
        ocorr = {canon(other["options"][c]) for c in other["correct_answers"]}
        if corr == ocorr:
            return other
    return None


def validate(q):
    where = q["question"][:60]
    assert q["difficulty"] in VALID_DIFF, where
    assert q["points"] in DIFF_POINTS[q["difficulty"]], where
    assert q["type"] in ("single_choice", "multiple_choice"), where
    assert q.get("source") in VALID_SOURCE, (where, q.get("source"))
    assert q.get("explanation"), ("missing explanation", where)
    assert q["explanation"].rstrip().endswith("."), ("explanation needs a full stop", where)
    assert len(q["options"]) == 4, (where, len(q["options"]))
    assert sorted(q["options"]) == ["A", "B", "C", "D"], (where, sorted(q["options"]))
    for c in q["correct_answers"]:
        assert c in q["options"], (where, c)
    # SS26 format: exactly one correct option, never a select-all prompt.
    assert q["type"] == "single_choice", (where, q["type"])
    assert len(q["correct_answers"]) == 1, where
    assert "select all" not in q["question"].lower(), where
    if q["source"] == "exercises":
        assert q.get("exercise") in (0, 1, 2, 3, 4), (where, q.get("exercise"))
    assert q["topic"] not in data["meta"]["excluded_topics"], (where, q["topic"])


# Purge multi-select before validating, since validate() now enforces the
# single-answer SS26 format.
purged = sum(1 for q in existing if q["type"] == "multiple_choice")
existing = [q for q in existing if q["type"] != "multiple_choice"]

# validate what is already in the bank too, so a bad hand edit is caught
for q in existing:
    validate(q)

# The SS26 instructions state that every question has exactly one correct
# option and that marking more than one scores zero. Multi-select questions are
# therefore dropped; questions_singleanswer.py covers the same material in the
# format the exam actually uses.
dropped_multi = 0

added = 0
skipped_exact = 0
skipped_near = []
for q in E + E2 + X + K + S:
    if q["type"] == "multiple_choice":
        dropped_multi += 1
        continue
    if canon(q["question"]) in seen:
        skipped_exact += 1
        continue
    validate(q)
    dup = near_duplicate(q, existing) or same_option_set(q, existing)
    if dup:
        skipped_near.append((q["question"][:58], dup.get("id", dup["question"][:40])))
        continue
    existing.append(q)
    seen.add(canon(q["question"]))
    added += 1

# ---- enforce the excluded topics ------------------------------------------
# The course notes leave four topics out entirely, so a question is dropped if
# answering it would require that material, whatever topic it is filed under.
def needs_excluded(q):
    blob = (q["question"] + " " + " ".join(q["options"].values()) + " " +
            q["explanation"]).lower()
    return [kw for kw in EXCLUDED_KEYWORDS if kw in blob]


dropped = [(q["question"][:58], needs_excluded(q)) for q in existing if needs_excluded(q)]
existing = [q for q in existing if not needs_excluded(q)]


# re-id sequentially
for i, q in enumerate(existing, start=1):
    q["id"] = f"q{i:04d}"

data["questions"] = existing
data["meta"]["generated_by"] = (
    "hand-written seed set + questions adapted from past exams (SS21-SS22, mock) "
    "+ questions grounded in the lecture notes "
    "+ questions grounded in the programming exercises 0-4"
)
data["meta"]["sources"] = sorted(VALID_SOURCE)
json.dump(data, open(BANK, "w"), indent=2, ensure_ascii=False)

# ---- report -----------------------------------------------------------------
n = len(existing)
byd = Counter(q["difficulty"] for q in existing)
byt = Counter(q["topic"] for q in existing)
bys = Counter(q["source"] for q in existing)
byx = Counter(q.get("exercise") for q in existing if q["source"] == "exercises")
pr = data["meta"]["priority"]

print(f"Added {added} new questions. Bank now: {n}")
print(f"Skipped {skipped_exact} exact duplicates, {len(skipped_near)} near duplicates.")
print(f"Dropped {len(dropped)} questions needing excluded topics.")
print(f"Dropped {dropped_multi} multi-select from source modules, purged {purged} already in the bank")
print("  (SS26 allows exactly one correct option; marking more scores zero)")
for txt, kws in dropped:
    print(f"    [{', '.join(kws)}] {txt}")
for txt, other in skipped_near:
    print(f"    near-dup of {other}: {txt}")


print("Difficulty:", {k: f"{v} ({v/n:.0%})" for k, v in byd.items()})
print("Type:", dict(Counter(q["type"] for q in existing)))
print("Source:", dict(bys))
print("Exercise questions per sheet:", dict(sorted(byx.items())))
print("By topic:")
for t, c in sorted(byt.items(), key=lambda kv: (pr.get(kv[0], "z"), kv[0])):
    print(f"  {pr.get(t,'?'):<4} {t}: {c}")

# ---- per-source difficulty spread, so the filtered modes stay usable --------
print("\nDifficulty x source (count and points available):")
grid = defaultdict(Counter)
pts = defaultdict(Counter)
for q in existing:
    grid[q["source"]][q["difficulty"]] += 1
    pts[q["source"]][q["difficulty"]] += q["points"]
for s in sorted(grid):
    row = grid[s]
    total = sum(pts[s].values())
    print(f"  {s:<14} " + " ".join(f"{d}={row[d]:>3}({pts[s][d]:>3}p)"
                                   for d in ("basics", "intermediate", "advanced"))
          + f"  total {total}p")

# ---- simulate a 100-pt mixed paper with the app's algorithm -----------------
MIXED = {"basics": .45, "intermediate": .35, "advanced": .20}


def assemble(target, pool):
    byDiff = {"basics": [], "intermediate": [], "advanced": []}
    for q in pool:
        byDiff[q["difficulty"]].append(q)
    for b in byDiff.values():
        random.shuffle(b)
    picked, used, p, guard = [], set(), 0, 0

    def draw(d):
        for q in byDiff[d]:
            if q["id"] not in used:
                used.add(q["id"])
                return q
        return None

    while p < target and guard < 3000:
        guard += 1
        best, pd = -1e9, "basics"
        for d, share in MIXED.items():
            cur = sum(q["points"] for q in picked if q["difficulty"] == d)
            deficit = share * target - cur
            if deficit > best:
                best, pd = deficit, d
        q = draw(pd) or draw("basics") or draw("intermediate") or draw("advanced")
        if not q:
            break
        picked.append(q)
        p += q["points"]
    return picked, p


print("\nSimulated 100-pt mixed papers:")
for label, pool in (("all", existing),
                    ("exercises only", [q for q in existing if q["source"] == "exercises"]),
                    ("past exams only", [q for q in existing if q["source"] == "past exams"])):
    for trial in range(2):
        p, tot = assemble(100, pool)
        pc = Counter()
        for q in p:
            pc[q["difficulty"]] += q["points"]
        shares = {k: round(pc[k] / tot, 2) for k in ("basics", "intermediate", "advanced")} if tot else {}
        print(f"  {label:<16} trial {trial+1}: {tot} pts / {len(p)} Qs -> {shares}")
