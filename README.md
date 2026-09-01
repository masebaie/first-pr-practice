# First PR Practice

A tiny repo for practicing the "clone, branch, fix, PR" workflow.

## What's here

`add.py` contains a single helper function, `add_numbers`, with a small test
suite in `test_add.py`.

## Usage

```bash
python add.py
```

## Running tests

```bash
python -m unittest test_add.py
```

This project is intentionally small so it's easy to receive your first pull
request end to end without worrying about a big codebase.

## Mounjaro tracker

`mounjaro-tracker.html` (also published as `mounjaro/index.html` for GitHub
Pages, kept in its own subfolder so it doesn't collide with any other app
published from this repo's root) is a self-contained, Arabic (RTL)
dashboard for tracking a Mounjaro weight-loss journey: a weight chart with
dose-phase bands, per-dose progress, an editable dose log, a full
searchable weigh-in log, and a form to log new entries (saved locally in
the browser). It's installable to an iOS home screen from Safari's Share
menu → "Add to Home Screen".

Open it directly in any browser:

```bash
open mounjaro-tracker.html   # or just double-click the file
```

Or, once GitHub Pages is enabled for this repo (Settings → Pages → Deploy
from branch → `master` / `/root`), it's live at its own dedicated path:

```
https://masebaie.github.io/first-pr-practice/mounjaro/
```
