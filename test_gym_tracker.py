import unittest

from gym_tracker import (
    add_attendance,
    add_payment,
    build_report,
    cost_per_session,
    session_count,
    total_payments,
)


class TestGymTracker(unittest.TestCase):
    def setUp(self):
        self.data = {"attendances": [], "payments": []}

    def test_add_attendance_counts_sessions(self):
        add_attendance(self.data, "2026-08-01")
        add_attendance(self.data, "2026-08-03")
        self.assertEqual(session_count(self.data), 2)

    def test_add_payment_sums_total(self):
        add_payment(self.data, 275, "monthly subscription")
        add_payment(self.data, 1230, "trainer")
        self.assertEqual(total_payments(self.data), 1505)

    def test_add_payment_rejects_non_positive(self):
        with self.assertRaises(ValueError):
            add_payment(self.data, 0)

    def test_cost_per_session_divides_total_by_count(self):
        add_payment(self.data, 275)
        add_payment(self.data, 1230)
        add_attendance(self.data, "2026-08-01")
        add_attendance(self.data, "2026-08-03")
        add_attendance(self.data, "2026-08-05")
        self.assertAlmostEqual(cost_per_session(self.data), 1505 / 3)

    def test_cost_per_session_with_no_sessions_is_none(self):
        add_payment(self.data, 275)
        self.assertIsNone(cost_per_session(self.data))

    def test_build_report_includes_key_numbers(self):
        add_payment(self.data, 275)
        add_attendance(self.data, "2026-08-01")
        report = build_report(self.data)
        self.assertIn("Sessions attended: 1", report)
        self.assertIn("Total payments: 275.00", report)
        self.assertIn("Cost per session: 275.00", report)


if __name__ == "__main__":
    unittest.main()
