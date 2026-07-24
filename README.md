# Deep Learning MCQ Trainer

Practice tool for the Deep Learning exam (SS26). Instead of a fixed set of past-paper questions you eventually memorise, this draws a fresh paper from a bank every time you sit down.

It's a single HTML page. No server, no install, no database — it runs entirely in the browser and is hosted on GitHub Pages. Your name and past scores live in your own browser.

## Built to the SS26 exam rules

The official exam notes drive several design decisions, so they are worth stating up front:

- **One correct option per question.** Rule B says marking more than one scores zero, so the bank is 100% single-answer. This is enforced, not just intended: `merge_bank.py` refuses to add a multi-select question and `verify_bank.py` fails the build if one appears.
- **Questions carry different points by difficulty**, as the real paper does. Basics are worth 1, intermediate 2–3, advanced 3–4.
- **100 points in 90 minutes.** The trainer derives its time limit from the same ratio, so a 40-point paper gives you 36 minutes automatically.
- **No negative marking.** Nothing is deducted for a wrong answer, so answering everything is always correct strategy — worth practising.
- **Topic priority and exclusions** follow the notes exactly (see below).

The exam also allows one handwritten A4 sheet, and the exercise bonus (up to 6 points) only counts if you already pass on the exam alone. Neither affects the trainer, but both affect how you revise.

## What it does

- **A fresh paper each attempt.** Questions are sampled and shuffled, and the four options are reordered every sitting, so repeats can't be memorised by position.
- **Question source.** Sit the whole bank, or narrow to **exercises only**, **past exams only** or **lecture notes only**. Exercise practice can be narrowed further to a single sheet (0–4).
- **Exam modes.** A full 100-point paper, a custom point total (10 / 20 / 40 / 60 / 100), or a single-topic quiz.
- **Difficulty.** Basics, intermediate, advanced, or a **mixed** paper aiming for roughly 45% / 35% / 20% by points. Picking one level gives you only that level — if the pool runs dry the paper ends rather than quietly topping up from elsewhere.
- **Live pool readout.** Before you start, the setup panel shows how many questions and points your filters can supply, and warns when a combination is too thin to hold the mixed split.
- **Marks, per-topic and per-source breakdown, and answer review** with an explanation on every question.

## What's in the bank

**461 questions, 932 points.** Every question carries a `source` tag, which is what the source filter uses.

| Source | Questions | Where it comes from |
| --- | --- | --- |
| `lecture notes` | 229 | Written against the lecture markdown in `lectures/` |
| `past exams` | 145 | SS21, WS20/21, WS21/22, SS22 and the WiSe20/21 mock |
| `exercises` | 87 | The concepts taught by the programming exercises 0–4 |

Questions are written in the shapes the real papers use, not as definition recall:

- **Statement evaluation** — "Which statement about batch normalisation is FALSE?"
- **Scenario** — "You add batch normalisation and can suddenly train at ten times the old learning rate. What explains that?"
- **Design critique** — "Your binary classifier ends with ReLU, then sigmoid, thresholded at 0.5. Is this sensible?"
- **Calculation** — "Input width 32, kernel 3, stride 2, padding 1. What is the output width?"

**Exercise questions** test the concepts the sheets teach — the layer interface, where gradients come from, initialization, convolution arithmetic, regularization, recurrence, the PyTorch training loop — not trivia about file layout. Each records its sheet, so you can revise one at a time: sheet 0 (10), 1 (19), 2 (21), 3 (20), 4 (17).

**Past-exam answers** were checked against the official solution PDFs. Note that these are *adapted*, not reproduced: the papers' short-answer and multi-select sections had to be converted into the SS26 single-answer format, so only a handful match a paper word for word.

### Coverage against the SS26 priority list

| Chapter | Priority | Questions |
| --- | --- | --- |
| Neural Networks | High | 59 |
| Activation Functions & CNN | High | 57 |
| Loss and Optimization | High | 54 |
| Regularization | High | 47 |
| Recurrent Neural Networks | High | 43 |
| Unsupervised Learning | High | 37 |
| Common Practices | Low | 57 |
| Segmentation | Low | 28 |
| Architectures | Low | 24 |
| Deep Reinforcement Learning | Low | 19 |
| Visualization and Attention | Low | 16 |
| Introduction | *not on the list* | 20 |

**Excluded entirely**, per the notes: Weakly Supervised Learning, Known Operator Learning, Graph Neural Networks, Self-Supervised Learning. This is enforced — `merge_bank.py` drops any question whose text, options or explanation would need that material, whatever topic it is filed under.

`Introduction` is not on the official topic list. Its questions cover bias/variance and overfitting, which do appear under the High topics, so they are kept as warm-up. Filter them out if you'd rather not see them.

## Every question has the same shape

`merge_bank.py` asserts all of this before writing:

- exactly four options, keyed `A`–`D`
- exactly one correct answer, and no "select all" prompt (SS26 rule B)
- points matching the difficulty (basics 1, intermediate 2–3, advanced 3–4)
- a non-empty explanation ending in a full stop
- a valid `source`, plus an `exercise` number when the source is `exercises`
- no exact or near-duplicate of a question already in the bank

## Rebuilding and verifying

```bash
python scripts/merge_bank.py         # merge, validate, drop duplicates, re-id
python scripts/rebalance_options.py  # spread the correct answer across A-D
python scripts/verify_bank.py        # full audit; non-zero exit on any hard error
```

Run `verify_bank.py` before deploying. It fails on structural faults, a broken answer key, a duplicated or reworded question, a multi-select question, or excluded-topic leakage.

### What has been verified

- **Answer keys.** All numeric questions were recomputed by hand, 38 factual claims in the exercise-derived questions were matched against the exercise PDFs and slide decks, and the past-exam answers were checked against the official solutions.
- **Answer-position bias, fixed.** The bank was originally written answer-first, leaving 79% of correct answers on option B — you could score 79% by always picking B. Options are now spread to ~25% per position, and the app reshuffles them every sitting.
- **Duplicates removed.** Detection runs on both the question stem and the option set, since a reworded stem over identical options is still the same question.
- **Format compliance.** 45 multi-select questions were converted to single-answer, and the format is now enforced in both the merge and the verify step.

### Known limitations

Three things `verify_bank.py` can't fix for you, listed honestly:

1. **The correct answer is the longest option about 70% of the time** (median 17 characters longer). Correct answers tend to be fully qualified while distractors stay terse, so a student can beat the bank above chance by picking the wordiest option. Since SS26 has no negative marking, this matters more than usual. Fixing it means rewriting the short distractors on roughly 180 questions.
2. **Scenario framing is under-represented.** The papers use "you observe X" for about 29% of questions; this bank manages 21%. Roughly 40 more scenario questions would close it.
3. **Most answers were verified by one person.** The 145 past-exam questions have external ground truth from the solution PDFs. The other ~316 do not. A second reader spot-checking 40 random questions would tell you more about reliability than any script.

## Growing the bank

Two ways, neither of which exposes any API key to this repo.

**From the site.** Open the "Fresh questions" panel, paste your own OpenAI or Anthropic key, pick a topic and a count. Questions go straight from your browser to the provider, are saved into your browser's copy of the bank tagged `source: "generated"`, and a **Generated only** filter appears once you have some. Anything returned in the wrong shape is discarded.

**Locally, then commit.** To grow the shared bank:

```bash
export OPENAI_API_KEY=sk-...          # or ANTHROPIC_API_KEY=sk-ant-...
python scripts/generate_questions.py --provider openai --per-topic 40
```

Both paths feed the matching lecture notes into the prompt so new questions stay grounded in the course material. `.gitignore` is set up so keys and `.env` files can't be committed by accident.

## Running it

```bash
python -m http.server 8000     # then visit http://localhost:8000
```

Serving matters — opening `index.html` directly can block the `fetch` of `data/questions.json` under some browsers' file:// rules.

For deployment see **DEPLOY.md**.

## What's in here

```
index.html                        the whole app (UI + exam engine + optional generation)
data/questions.json               the question bank (461 questions)
lectures/                         course lecture notes; used to ground question generation
scripts/questions_exams.py        past-exam questions: the choice sections
scripts/questions_exams_extra.py  past-exam questions: short-answer and calculation parts
scripts/questions_exercises.py    concepts from the programming exercises 0-4
scripts/questions_chapters.py     exam-pattern questions across every chapter
scripts/questions_singleanswer.py single-answer replacements for the old multi-select set
scripts/merge_bank.py             merges everything into data/questions.json, with validation
scripts/rebalance_options.py      spreads the correct answer evenly across A-D
scripts/verify_bank.py            full pre-deployment audit
scripts/generate_questions.py     grows the bank with your own API key
DEPLOY.md                         GitHub Pages deployment guide
.nojekyll                         so GitHub Pages leaves the folders alone
```

---

Built for practice, not as a substitute for the real papers. Use the bank for breadth and the past-paper PDFs for timing. If a question looks wrong, it's a one-line fix in `data/questions.json` — go ahead and correct it.
