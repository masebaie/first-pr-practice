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

## Published apps (GitHub Pages)

GitHub Pages for this repo is set to **Deploy from a branch →
`claude/mounjaro-weight-tracker-ucseu6` → `/docs`**. Every small app here
publishes from a folder under `docs/` on *this* branch, so they all stay
live side by side at their own dedicated path — no more editing the Pages
branch setting to switch between them.

| App | Source | Live at |
|---|---|---|
| Mounjaro tracker | `docs/index.html` | https://masebaie.github.io/first-pr-practice/ |
| Gym journey | `docs/gym/index.html` | https://masebaie.github.io/first-pr-practice/gym/ |
| Duas (خزانة الأدعية) | `docs/duas/index.html` | https://masebaie.github.io/first-pr-practice/duas/ |

To add another app later: drop its files in a new `docs/<app-name>/`
folder (with its own `index.html`) on this same branch and push — no
Settings changes needed.

### Mounjaro tracker

`mounjaro-tracker.html` (also published as `docs/index.html`) is a
self-contained, Arabic (RTL) dashboard for tracking a Mounjaro weight-loss
journey: a weight chart with dose-phase bands, per-dose progress, an
editable dose log, a full searchable weigh-in log, and a form to log new
entries (saved locally in the browser). It's installable to an iOS home
screen from Safari's Share menu → "Add to Home Screen". Open it directly
in any browser:

```bash
open mounjaro-tracker.html   # or just double-click the file
```
