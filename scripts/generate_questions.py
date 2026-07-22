#!/usr/bin/env python3
"""
Grow the question bank with an LLM, using YOUR OWN key.

The key is read from an environment variable and is never written to disk or
committed. New questions are appended to data/questions.json.

Usage
-----
  # OpenAI
  export OPENAI_API_KEY=sk-...
  python scripts/generate_questions.py --provider openai --per-topic 40

  # Anthropic
  export ANTHROPIC_API_KEY=sk-ant-...
  python scripts/generate_questions.py --provider anthropic --per-topic 40

Only high/low priority (non-excluded) topics are targeted. High-priority topics
get the full --per-topic count; low-priority topics get about 60% of it, so the
bank naturally stays weighted the way the course notes suggest.
"""

import argparse, json, os, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_PATH = os.path.join(HERE, "..", "data", "questions.json")
LECTURE_DIR = os.path.join(HERE, "..", "lectures")

DIFF_POINTS = {"basics": [1], "intermediate": [2, 3], "advanced": [3, 4]}

# Topic -> lecture notes file; used to ground the generation prompt in the
# actual course material instead of the model's general knowledge.
LECTURE_FILES = {
    "Introduction": "0_Intro.md",
    "Neural Networks": "1_NeuralNetworks.md",
    "Loss and Optimization": "2_LossAndOptimization.md",
    "Activation Functions and CNN": "3_CNNs.md",
    "Regularization": "4_Regularization.md",
    "Common Practices": "5_CommonPractices.md",
    "Architectures": "6_Architectures.md",
    "Recurrent Neural Networks": "7_RecurrentNeuralNetworks.md",
    "Visualization and Attention Mechanism": "8_Visualization.md",
    "Deep Reinforcement Learning": "9_ReinforcementLearning.md",
    "Unsupervised Learning": "10_Unsupervised.md",
    "Segmentation": "11_SegmentationAndObjectDetection.md",
}


def lecture_excerpt(topic, max_chars=9000):
    """Return a excerpt of the topic's lecture notes, or '' when unavailable."""
    fname = LECTURE_FILES.get(topic)
    if not fname:
        return ""
    path = os.path.join(LECTURE_DIR, fname)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()[:max_chars]

EXCLUDED_TOPICS = ["Weakly Supervised Learning", "Known Operator Learning",
                   "Graph Neural Networks", "Self-Supervised Learning"]

PROMPT_TMPL = (
    'Create {n} exam-quality multiple-choice questions on the deep learning topic "{topic}". '
    'Roughly 45% basics, 35% intermediate, 20% advanced. Mostly single_choice with a few '
    'multiple_choice. Use plausible distractors that reflect real misconceptions rather than '
    'obviously wrong filler.\n'
    'Return ONLY a JSON array, no markdown fences, each item exactly:\n'
    '{{"topic":"{topic}","difficulty":"basics|intermediate|advanced",'
    '"points":<int: 1 basics, 2-3 intermediate, 3-4 advanced>,'
    '"type":"single_choice|multiple_choice","question":"...",'
    '"options":{{"A":"...","B":"...","C":"...","D":"..."}},'
    '"correct_answers":["A"],"explanation":"..."}}\n'
    'Rules:\n'
    '- Always exactly four options keyed A, B, C, D. Never more, never fewer.\n'
    '- single_choice has exactly one correct answer. multiple_choice has two or three,\n'
    '  and its question text must end with "(Select all that apply)".\n'
    '- Every item needs a non-empty explanation of one or two sentences ending in a full stop.\n'
    '- Option texts must not end with a full stop.\n'
    '- Do not write questions that require {excluded}; those topics are out of scope.'
)


def post(url, headers, payload):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=headers, method="POST"
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def call_openai(key, prompt):
    data = post(
        "https://api.openai.com/v1/chat/completions",
        {"Content-Type": "application/json", "Authorization": "Bearer " + key},
        {"model": "gpt-4o-mini",
         "messages": [{"role": "user", "content": prompt}],
         "temperature": 0.7},
    )
    return data["choices"][0]["message"]["content"]


def call_anthropic(key, prompt):
    data = post(
        "https://api.anthropic.com/v1/messages",
        {"Content-Type": "application/json", "x-api-key": key,
         "anthropic-version": "2023-06-01"},
        {"model": "claude-3-5-sonnet-20241022", "max_tokens": 3000,
         "messages": [{"role": "user", "content": prompt}]},
    )
    return "".join(b.get("text", "") for b in data["content"])


def clean(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
    return text.strip()


def normalise(q, topic):
    """Coerce one generated item into the bank's shape, or return None.

    The bank is uniform (four options A-D, one explanation, a source tag), and
    the app relies on that. Anything that cannot be repaired is dropped rather
    than written out in a shape the review screen cannot render.
    """
    if not isinstance(q, dict):
        return None
    if not isinstance(q.get("question"), str) or not q["question"].strip():
        return None
    opts = q.get("options")
    if not isinstance(opts, dict) or sorted(opts) != ["A", "B", "C", "D"]:
        return None
    if any(not isinstance(v, str) or not v.strip() for v in opts.values()):
        return None

    diff = q.get("difficulty") if q.get("difficulty") in DIFF_POINTS else "intermediate"
    allowed = DIFF_POINTS[diff]
    try:
        pts = int(q.get("points", allowed[0]))
    except (TypeError, ValueError):
        pts = allowed[0]
    if pts not in allowed:
        pts = allowed[0]

    corr = q.get("correct_answers")
    if not isinstance(corr, list):
        return None
    corr = sorted({c for c in corr if c in opts})
    if not corr or len(corr) >= 4:
        return None

    qtype = "multiple_choice" if len(corr) > 1 else "single_choice"
    text = q["question"].strip()
    if qtype == "multiple_choice" and "select all that apply" not in text.lower():
        text = text.rstrip() + " (Select all that apply)"
    if qtype == "single_choice" and "select all that apply" in text.lower():
        return None

    expl = q.get("explanation")
    expl = expl.strip() if isinstance(expl, str) else ""
    if not expl:
        expl = "Generated question - no explanation was supplied."
    if not expl.endswith((".", "!", "?")):
        expl += "."

    return {
        "topic": topic,
        "difficulty": diff,
        "points": pts,
        "type": qtype,
        "question": text,
        "options": {k: v.strip().rstrip(".") for k, v in opts.items()},
        "correct_answers": corr,
        "explanation": expl,
        "source": "generated",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["openai", "anthropic"], required=True)
    ap.add_argument("--per-topic", type=int, default=40,
                    help="questions per high-priority topic")
    args = ap.parse_args()

    env = "OPENAI_API_KEY" if args.provider == "openai" else "ANTHROPIC_API_KEY"
    key = os.environ.get(env)
    if not key:
        sys.exit(f"Set {env} in your environment first (it is never written to disk).")

    bank = json.load(open(BANK_PATH))
    priority = bank["meta"]["priority"]
    existing = bank["questions"]
    next_num = len(existing) + 1

    caller = call_openai if args.provider == "openai" else call_anthropic
    added = 0

    for topic, pr in priority.items():
        if topic in EXCLUDED_TOPICS:
            continue
        n = args.per_topic if pr == "high" else max(5, int(args.per_topic * 0.6))
        print(f"→ {topic} ({pr}): requesting {n} …", flush=True)
        prompt = PROMPT_TMPL.format(n=n, topic=topic,
                                   excluded=', '.join(EXCLUDED_TOPICS))
        excerpt = lecture_excerpt(topic)
        if excerpt:
            prompt = ("Base the questions on the following lecture notes "
                      "(stay within this material):\n" + excerpt + "\n\n" + prompt)
        try:
            raw = caller(key, prompt)
            items = json.loads(clean(raw))
        except (urllib.error.HTTPError, json.JSONDecodeError, KeyError) as e:
            print(f"   skipped ({e})")
            continue
        seen = {e["question"].strip() for e in existing}
        good = []
        for item in items if isinstance(items, list) else []:
            q = normalise(item, topic)
            if q and q["question"].strip() not in seen:
                seen.add(q["question"].strip())
                good.append(q)
        for q in good:
            q["id"] = f"q{next_num:04d}"
            next_num += 1
            existing.append(q)
        added += len(good)
        n_raw = len(items) if isinstance(items, list) else 0
        print(f"   added {len(good)} (of {n_raw} returned)")
        time.sleep(1)

    bank["questions"] = existing
    bank["meta"]["generated_by"] = f"{bank['meta'].get('generated_by','')}; +{added} via {args.provider}"
    json.dump(bank, open(BANK_PATH, "w"), indent=2, ensure_ascii=False)
    print(f"\nDone. Bank is now {len(existing)} questions (+{added}).")
    print("Commit data/questions.json to publish the bigger bank.")


if __name__ == "__main__":
    main()
