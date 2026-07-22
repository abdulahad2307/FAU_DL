"""Remove answer-position bias from the bank.

The bank was written answer-first, which left 79% of correct answers sitting on
option B and made the paper gameable without any knowledge of the subject. This
redistributes the options so the correct answer lands roughly uniformly across
A-D.

Two rules:

* Option sets that are entirely numeric are sorted ascending, which is what a
  real exam does and which spreads the correct value naturally by its rank.
* Everything else is permuted with a seeded shuffle, so re-running the script
  gives the same bank rather than churning the diff.

The permutation is chosen to flatten the overall distribution rather than being
drawn blindly, otherwise a random shuffle of 500 questions still leaves visible
lumps.

Run after merge_bank.py. Safe to re-run.
"""

import json
import os
import random
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "data", "questions.json")
KEYS = ["A", "B", "C", "D"]
SEED = 20260722


def is_numeric_set(options):
    return all(re.fullmatch(r"[-+]?\d*\.?\d+", v.strip()) for v in options.values())


def reorder(q, new_order):
    """new_order[i] is the old key that should now sit at KEYS[i]."""
    old_opts = q["options"]
    remap = {old: KEYS[i] for i, old in enumerate(new_order)}
    q["options"] = {KEYS[i]: old_opts[old] for i, old in enumerate(new_order)}
    q["correct_answers"] = sorted(remap[c] for c in q["correct_answers"])


def main():
    rng = random.Random(SEED)
    data = json.load(open(BANK))
    qs = data["questions"]

    before = Counter(q["correct_answers"][0] for q in qs if q["type"] == "single_choice")

    numeric_sorted = 0
    # Deal out target positions so single-choice answers land evenly, instead of
    # trusting a blind shuffle to come out flat.
    singles = [q for q in qs if q["type"] == "single_choice" and not is_numeric_set(q["options"])]
    rng.shuffle(singles)
    targets = [KEYS[i % 4] for i in range(len(singles))]
    rng.shuffle(targets)
    target_of = {id(q): t for q, t in zip(singles, targets)}

    for q in qs:
        if is_numeric_set(q["options"]):
            order = sorted(q["options"], key=lambda k: float(q["options"][k].strip()))
            reorder(q, order)
            numeric_sorted += 1
            continue

        want = target_of.get(id(q))
        others = [k for k in KEYS if k not in q["correct_answers"]]
        rng.shuffle(others)

        if want and len(q["correct_answers"]) == 1:
            correct = q["correct_answers"][0]
            order = others[:]
            order.insert(KEYS.index(want), correct)
        else:
            order = KEYS[:]
            rng.shuffle(order)
        reorder(q, order)

    after = Counter(q["correct_answers"][0] for q in qs if q["type"] == "single_choice")
    n = sum(after.values())

    json.dump(data, open(BANK, "w"), indent=2, ensure_ascii=False)

    print(f"Rebalanced {len(qs)} questions ({numeric_sorted} numeric sets sorted ascending).")
    print("Correct-answer position, single choice:")
    for k in KEYS:
        print(f"  {k}: {before[k]:>3} ({before[k]/n:>5.1%})  ->  {after[k]:>3} ({after[k]/n:>5.1%})")


if __name__ == "__main__":
    main()
