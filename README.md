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

## Gym tracker

`gym_tracker.py` logs your gym visits and payments (subscription, trainer,
etc.) in a local `gym_data.json` file, and computes your cost per session
as total payments divided by sessions attended.

```bash
# log a visit (defaults to today)
python gym_tracker.py attend

# log a visit for a specific date
python gym_tracker.py attend --date 2026-08-09

# log a payment
python gym_tracker.py pay 275 --desc "monthly subscription"
python gym_tracker.py pay 1230 --desc "trainer, 4x/week"

# see the report
python gym_tracker.py report
```

Example output:

```
Sessions attended: 3
Total payments: 1505.00
Cost per session: 501.67
```

Run its tests with:

```bash
python -m unittest test_gym_tracker.py
```

## Gym tracker mobile app

`webapp/index.html` is a self-contained, mobile-first web app version of the
same idea: log sessions and payments and see the cost per session, all from
your phone. Data is saved in the browser's `localStorage` (nothing leaves
your device), with an export/import button for backups.

Open it by downloading `webapp/index.html` and opening it in a mobile
browser, or host it (e.g. GitHub Pages) and use Safari's "Add to Home
Screen" on iPhone to use it like an app.
