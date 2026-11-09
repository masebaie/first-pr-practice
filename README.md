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

## Expressions app (تعبيراتي)

`docs/expressions/` is an installable Arabic (RTL) web app for keeping a
personal table of English expressions and their Arabic meanings:

- Add, edit, and delete expressions (with an undo after deleting), each with
  an optional example sentence and note.
- Live search in English or Arabic (ignores case, diacritics, and
  alef/ya/ta-marbuta variants) with the match highlighted.
- Favorites, newest / A→Z sorting, and a speaker button that reads the
  English expression aloud.
- Same palette as the gym tracker (slate, emerald, and the violet→pink→cyan
  gradient), with light and dark
  themes. A table on wide screens, cards on phones.
- Works offline and keeps data on the device only, with JSON backup and
  restore.

Live at:

```
https://masebaie.github.io/first-pr-practice/expressions/
```

On iPhone: open it in Safari → Share → "Add to Home Screen". On Android:
Chrome → ⋮ → "Install app".

## Vault (خزنتي)

`docs/vault/` is an installable, Arabic (RTL) password vault for the phone:

- Every account is a card with its fields (username, password, PIN, …); one
  tap copies a value, and secret fields stay masked until you tap 👁️.
- Add, edit, and delete accounts, with any number of fields each, a category,
  and a strong-password generator.
- Search plus colour-coded category filters, in the gym tracker's palette
  (slate, emerald, and the violet→pink→cyan gradient), light and dark.
- Data is encrypted on the device with a master password (PBKDF2-SHA256 with
  600,000 iterations + AES-256-GCM) and never leaves it; a Content Security
  Policy blocks the page from sending anything to other servers.
- The master password must be strong (10+ characters, mixing upper and lower
  case, digits, and symbols). Five wrong attempts trigger an increasing
  lockout.
- Locks after 3 minutes idle or 30 seconds away; the screen is hidden while
  the app is in the background, and copied values are cleared from the
  clipboard after 45 seconds.
- Import a plain JSON list of accounts on first run (encrypted right away),
  and export or restore an encrypted backup.
- Works offline.

**No account data is stored in this repo**; the app ships empty.

Live at:

```
https://masebaie.github.io/first-pr-practice/vault/
```

On iPhone: open it in Safari → Share → "Add to Home Screen". On Android:
Chrome → ⋮ → "Install app".
