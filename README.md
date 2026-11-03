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

`mounjaro-tracker.html` (also published as `docs/mounjaro/index.html` for
GitHub Pages) is a self-contained, Arabic (RTL) dashboard for tracking a
Mounjaro weight-loss journey: a weight chart with dose-phase bands,
per-dose progress, an editable dose log, a full searchable weigh-in log,
and a form to log new entries (saved locally in the browser). It's
installable to an iOS home screen from Safari's Share menu → "Add to Home
Screen".

Open it directly in any browser:

```bash
open mounjaro-tracker.html   # or just double-click the file
```

Or, with GitHub Pages set to **Deploy from a branch → `master` / `/docs`**
(Settings → Pages), it's live at its own dedicated path:

```
https://masebaie.github.io/first-pr-practice/mounjaro/
```

Every other small app in this repo should publish under its own
`docs/<app-name>/` folder the same way, so they all stay live
simultaneously without fighting over the Pages branch/folder setting.

## Zakat app (زكاتي)

`docs/zakat/` is an installable Arabic (RTL) web app for calculating yearly
zakat and logging what was paid:

- A calculator for gold (by karat), cash and savings, and trade real estate,
  minus bank, car, and mortgage financing (by default only the next 12
  months of installments are deducted).
- A payments log per zakat year (1 Ramadan → end of Sha'ban, calculation
  day on the next 1 Ramadan, Umm al-Qura calendar). Each payment records
  its date, amount, and recipient, and is grouped by Hijri month.
- Works offline (service worker) and keeps data on the device only, with
  a backup/restore button that exports a JSON file.

Live at:

```
https://masebaie.github.io/first-pr-practice/zakat/
```

On iPhone: open it in Safari → Share → "Add to Home Screen".
