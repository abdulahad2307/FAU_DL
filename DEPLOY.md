# Deploying to GitHub Pages

The trainer is a static site — one HTML file plus a JSON bank — so GitHub Pages
hosts it for free with no build step. Total time: about five minutes.

## Prerequisites

- A GitHub account
- Git installed locally (`git --version` to check), **or** just a browser —
  Option B below needs no Git at all

---

## Option A — with Git (recommended)

### 1. Verify the bank

```bash
cd deep-learning-mcq-trainer
python scripts/verify_bank.py
```

It must end with `PASSED`. If it doesn't, fix what it lists before deploying.

### 2. Test locally

```bash
python -m http.server 8000
```

Open http://localhost:8000 — enter a name, start a short 10-point paper, submit
it, and check the review screen shows explanations. Don't skip this: opening
`index.html` directly via file:// can behave differently from a served site,
and Pages serves.

### 3. Create the repository

On github.com → **+** → **New repository**:

- Name: `dl-mcq-trainer` (anything works; it becomes part of your URL)
- Visibility: **Public** (Pages on private repos needs a paid plan)
- Do **not** initialise with a README — the folder already has one

### 4. Push the folder

```bash
cd deep-learning-mcq-trainer
git init
git add .
git commit -m "Deep Learning MCQ trainer"
git branch -M main
git remote add origin https://github.com/<YOUR-USERNAME>/dl-mcq-trainer.git
git push -u origin main
```

The `.gitignore` already excludes `.env` and key files, so an accidentally
saved API key can't be committed.

### 5. Turn on Pages

On the repo page: **Settings → Pages** (left sidebar):

- Source: **Deploy from a branch**
- Branch: **main**, folder **/ (root)**
- **Save**

### 6. Wait, then open

Pages takes 1–3 minutes on the first deploy. The URL appears at the top of the
Pages settings page:

```
https://<YOUR-USERNAME>.github.io/dl-mcq-trainer/
```

### 7. Verify the live site

Open the URL and sit a short paper end to end. If the page loads but shows
"bank: 0 questions" in the footer, see Troubleshooting below.

---

## Option B — no Git, browser only

1. Create the repository as in step 3 above.
2. On the empty repo page, click **uploading an existing file**.
3. Drag the **contents** of the `deep-learning-mcq-trainer` folder in — the
   folder's contents, not the folder itself, so `index.html` sits at the repo
   root. GitHub keeps the `data/`, `lectures/` and `scripts/` structure.
4. Commit, then continue from step 5 above.

Note: drag-and-drop can silently skip dotfiles. After uploading, check that
`.nojekyll` appears in the file list; if not, create it via **Add file →
Create new file**, name it `.nojekyll`, leave it empty, commit.

---

## Updating the site later

Any push to `main` redeploys automatically:

```bash
# after editing questions or scripts
python scripts/merge_bank.py
python scripts/rebalance_options.py
python scripts/verify_bank.py        # must PASS
git add data/questions.json
git commit -m "Grow the bank"
git push
```

Give it a minute, then hard-refresh the site (Ctrl+Shift+R / Cmd+Shift+R) —
browsers cache the JSON.

---

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| 404 at the site URL | Pages not enabled yet, or still building | Settings → Pages: check a build is listed; wait 3 min |
| Page loads, footer says "bank: 0 questions" | `data/questions.json` didn't upload, or `.nojekyll` is missing so Pages mangles the folders | Check both files exist in the repo at the right paths |
| Site is stale after a push | Browser cache | Hard refresh; check the Actions tab shows the `pages-build-deployment` run finished |
| Works locally, blank on Pages | You pushed the folder *inside* another folder | `index.html` must be at the repo root, or set Pages folder accordingly |
| "Fresh questions" generation fails | Key pasted wrong, or provider CORS | The error message names the cause; keys never touch the repo either way |
| Someone's history/name disappeared | Data lives in *their* browser's localStorage | Expected — different browser or device means a fresh profile |

## Two things worth knowing

- **Everything in the repo is public.** That includes the question bank and
  the lecture notes in `lectures/`. If the notes shouldn't be public, delete
  `lectures/` before pushing — the app runs fine without it; only the
  "generate from lecture notes" grounding stops working.
- **There is no server.** Scores, names and generated questions live in each
  visitor's own browser. Nothing is collected, so there is also nothing to
  back up — warn users that clearing site data wipes their history.
