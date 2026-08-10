"""Track gym attendance and payments, and compute cost per session."""
import argparse
import json
import os
from datetime import date

DEFAULT_DATA_FILE = "gym_data.json"


def load_data(path=DEFAULT_DATA_FILE):
    if not os.path.exists(path):
        return {"attendances": [], "payments": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data, path=DEFAULT_DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_attendance(data, on_date=None):
    data["attendances"].append(on_date or date.today().isoformat())
    return data


def add_payment(data, amount, description=""):
    if amount <= 0:
        raise ValueError("amount must be positive")
    data["payments"].append({"amount": amount, "description": description})
    return data


def total_payments(data):
    return sum(p["amount"] for p in data["payments"])


def session_count(data):
    return len(data["attendances"])


def cost_per_session(data):
    count = session_count(data)
    if count == 0:
        return None
    return total_payments(data) / count


def build_report(data):
    count = session_count(data)
    total = total_payments(data)
    cost = cost_per_session(data)
    lines = [
        f"Sessions attended: {count}",
        f"Total payments: {total:.2f}",
    ]
    if cost is None:
        lines.append("Cost per session: N/A (no sessions logged yet)")
    else:
        lines.append(f"Cost per session: {cost:.2f}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Track gym attendance and cost per session.")
    parser.add_argument("--file", default=DEFAULT_DATA_FILE, help="path to data file")
    sub = parser.add_subparsers(dest="command", required=True)

    attend = sub.add_parser("attend", help="log a gym visit")
    attend.add_argument("--date", help="date of visit (YYYY-MM-DD), defaults to today")

    pay = sub.add_parser("pay", help="log a payment")
    pay.add_argument("amount", type=float, help="payment amount")
    pay.add_argument("--desc", default="", help="payment description")

    sub.add_parser("report", help="show attendance and cost report")

    args = parser.parse_args()
    data = load_data(args.file)

    if args.command == "attend":
        add_attendance(data, args.date)
        save_data(data, args.file)
        print("Visit logged.")
    elif args.command == "pay":
        add_payment(data, args.amount, args.desc)
        save_data(data, args.file)
        print("Payment logged.")
    elif args.command == "report":
        print(build_report(data))


if __name__ == "__main__":
    main()
