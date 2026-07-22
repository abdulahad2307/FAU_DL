# Deep Learning MCQ Trainer

A practice tool for the Deep Learning course (SS2026). Instead of a fixed set of past-paper questions you eventually memorise, this pulls from a bank and shuffles a fresh paper every time you sit down. Sit it ten times and you shouldn't keep seeing the same ten questions.

It's a single HTML page. No server, no install, no database — it runs entirely in the browser and I host it on GitHub Pages. Your name and past scores live in your own browser, not on any server I control.

## What it does

- **Fresh papers each attempt.** Questions are sampled and shuffled from the bank, so repeats are rare.
- **Question source.** Sit the whole bank, or narrow the draw to **exercises only**, **past exams only**, or **lecture notes only**. Exercise practice can be narrowed further to a single sheet (0–4).
- **Exam modes.** A full 100-point / 90-minute paper, a custom point total (10 / 20 / 40 / 60 / 100), or a single-topic quiz. Time is worked out from the same ratio the real exam uses — 90 minutes per 100 points — so a 40-point paper gives you 36 minutes automatically.
- **Difficulty.** Basics, intermediate, advanced, or a **mixed** paper that aims for roughly 45% basics / 35% intermediate / 20% advanced by points. Picking a single level now gives you *only* that level — if the pool runs out the paper simply ends, rather than quietly topping up from the other levels.
- **Single or multiple choice.** Pick one, the other, or let it hand you both.
- **Point-weighted questions.** Basics are worth 1 point, intermediate 2–3, advanced 3–4. Always whole points, shown next to each question.
- **Live pool readout.** Before you start, the setup panel tells you how many questions and points your current filters can actually supply, and warns when a combination is too thin to hold the 45/35/20 split.
- **Marks, per-topic and per-source breakdown, and answer review** with explanations at the end. Every question in the bank has an explanation.

## How the questions were built

The bank ships with **498 validated questions** (971 points) drawn from four sources. Every question carries a `"source"` tag, which is what the source filter uses.

| Source | Questions | Points | Where it comes from |
| --- | --- | --- | --- |
| `exercises` | 158 | 300 | The programming exercises 0–4 |
| `past exams` | 145 | 297 | SS21, WS20/21, WS21/22, SS22 and the WiSe20/21 mock |
| `lecture notes` | 116 | 219 | Original questions written against the lecture markdown in `lectures/` |
| `seed` | 79 | 155 | A hand-written set covering the fundamentals |

**Exercise questions** are grounded in the exercise descriptions, the exercise slide decks and the provided skeleton code — the layer-oriented framework you build by hand (Sgd, BaseLayer, FullyConnected, ReLU, SoftMax, CrossEntropyLoss, NeuralNetwork, then Initializers, Adam, Conv, Pooling, Flatten, then L1/L2, Dropout, BatchNorm, TanH/Sigmoid, RNN, LSTM) and the PyTorch ResNet challenge. This is worth practising separately: the exam has a coding section that says outright that you're given "the framework of the exercise 1, 2 and 3". Each one also records which sheet it came from:

| Sheet | Topic | Questions |
| --- | --- | --- |
| 0 | NumPy patterns & ImageGenerator | 22 |
| 1 | Basic framework | 29 |
| 2 | CNN layers, initializers & optimizers | 37 |
| 3 | Regularization, batch norm & RNN | 40 |
| 4 | PyTorch / ResNet challenge | 30 |

**Past-exam questions** have their answers checked against the official solution PDFs. The single- and multiple-choice sections convert directly; the short-answer, numeric and derivation parts were rewritten as multiple choice.

Topics are weighted the way the exam notes suggest:

- **Heavier coverage:** Neural Networks, Loss & Optimization, Activation Functions & CNNs, Regularization, RNNs, Unsupervised Learning (plus the Introduction).
- **Lighter coverage:** Common Practices, Architectures, Visualization & Attention, Deep Reinforcement Learning, Segmentation.
- **Left out entirely:** Weakly Supervised Learning, Known Operator Learning, Graph Neural Networks, Self-Supervised Learning.

The exclusion is enforced, not just documented: `merge_bank.py` drops any question whose text, options or explanation would require that material, whatever topic it's filed under.

The bank ships as a plain JSON file (`data/questions.json`). Nothing clever is hidden — you can open it and read every question, answer and explanation.

## Every question has the same shape

The app relies on the bank being uniform, so `merge_bank.py` asserts all of this before writing:

- exactly four options, keyed `A`, `B`, `C`, `D`
- `single_choice` has exactly one correct answer; `multiple_choice` has two or three and says "(Select all that apply)" in the question text
- points match the difficulty (basics 1, intermediate 2–3, advanced 3–4)
- a non-empty explanation ending in a full stop
- a valid `source`, plus an `exercise` number when the source is `exercises`
- no exact or near-duplicate of a question already in the bank

Both generation paths below produce and validate the same shape, so questions you add yourself sit alongside the shipped ones without breaking the review screen or the source filters.

## Making the bank bigger (optional)

There are two ways to add questions, and **neither one touches my keys or exposes yours**.

**1. From the site itself.** Open the "Fresh questions" panel, paste your own OpenAI or Anthropic key, pick a topic and a count, and it generates questions straight from your browser to the provider. They're saved into your browser's copy of the bank, tagged `source: "generated"`, and a **Generated only** filter button appears once you have some. Anything the model returns in the wrong shape is discarded rather than added. Your key never leaves your machine and never comes near this repo.

**2. Locally, then commit.** To grow the *shared* bank that everyone downloads, run the script with your own key set as an environment variable:

```bash
export OPENAI_API_KEY=sk-...          # or ANTHROPIC_API_KEY=sk-ant-...
python scripts/generate_questions.py --provider openai --per-topic 40
```

It appends to `data/questions.json`, keeps the topic weighting, forces the point values into the right ranges and skips the excluded topics. Both generation paths feed the matching lecture notes from `lectures/` into the prompt, so new questions stay grounded in what the course actually covers rather than general internet knowledge. Commit the updated JSON and the bigger bank is live for everyone. The `.gitignore` is set up so keys and `.env` files can't be committed by accident.

## Running it

**Locally**, just open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

Serving it matters — opening the file directly can block the `fetch` of `data/questions.json` under some browsers' file:// rules.

**On GitHub Pages:**

1. Push this folder to a repo.
2. Settings → Pages → Build from branch → `main` / root.
3. The `.nojekyll` file is already here so Pages serves `data/` and `scripts/` untouched.
4. Your site goes live at `https://<username>.github.io/<repo>/`.

## What's in here

```
index.html                        the whole app (UI + exam engine + optional generation)
data/questions.json               the question bank (498 questions)
lectures/                         the course lecture notes; used to ground question generation
scripts/build_bank.py             rebuilds the hand-written seed set
scripts/questions_exams.py        past-exam questions: the choice sections
scripts/questions_exams_extra.py  past-exam questions: short-answer, numeric and coding parts
scripts/questions_lectures.py     questions written against the lecture notes
scripts/questions_exercises.py    questions from the programming exercises 0-4
scripts/backfill_seed.py          adds explanations and source tags to the seed set
scripts/merge_bank.py             merges everything into data/questions.json (with validation)
scripts/rebalance_options.py      spreads the correct answer evenly across A-D
scripts/verify_bank.py            full pre-deployment audit of the finished bank
scripts/generate_questions.py     grows the bank further with your own API key
.nojekyll                         so GitHub Pages leaves the folders alone
```

## Rebuilding and verifying the bank

```bash
python scripts/backfill_seed.py      # only needed once, or after editing the seed set
python scripts/merge_bank.py         # merge, validate, drop duplicates, re-id
python scripts/rebalance_options.py  # spread the correct answer across A-D
python scripts/verify_bank.py        # full audit; exits non-zero on any hard error
```

`merge_bank.py` validates every question, drops duplicates and excluded-topic material, re-assigns ids, and prints counts by topic, difficulty and source plus simulated 100-point papers for each filtered mode, so you can see the 45/35/20 split actually holds.

`verify_bank.py` re-checks the finished file end to end and is the one to run before deploying. It fails the build on structural faults, a broken answer key, a duplicated or reworded question, or excluded-topic leakage, and warns about the quality signals below.

### What was verified

- **Every answer key** was checked. All 11 questions with numeric options were recomputed by hand, and 38 specific factual claims in the exercise- and exam-derived questions (constructor argument orders, Xavier/He formulas, Adam defaults, dropout keep-probability, batch-norm epsilon, ResNet channel counts, padding conventions and so on) were matched against the exercise PDFs and the official exam solutions.
- **Answer-position bias, fixed.** The bank was originally written answer-first, which left **79% of correct answers on option B** — you could score 79% by always picking B without knowing any deep learning. Options are now redistributed to ~25% per position, *and* the app reshuffles them on every sitting, so repeat attempts can't be memorised by position and generated questions get the same treatment.
- **Duplicates removed.** Eleven duplicate or reworded-duplicate questions were found and dropped. Detection now runs on both the question stem and the option set, since a reworded stem over identical options is still the same question.
- **The difficulty filter was leaking.** Picking "Basics only" used to fall back to intermediate and advanced questions once the basics pool ran out. A single-difficulty paper now ends instead of quietly substituting.

### Known limitation

`verify_bank.py` reports one warning it cannot fix for you: **the correct answer is the longest option about 80% of the time** (median 31 characters longer than the distractors). Correct answers are fully qualified while distractors are terse, so a student can beat the bank well above chance by always picking the wordiest option. Fixing it means lengthening ~260 distractors so they read as specifically as the answer — worth doing, but it is a content edit on each question, not something a script can do safely. The check is in place so you can watch the number come down as you work through them.

---

Built for practice. If a question looks off, it's a one-line fix in `data/questions.json` — go ahead and correct it.
