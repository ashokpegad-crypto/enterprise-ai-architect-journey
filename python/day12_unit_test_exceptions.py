import unittest


def calculate_employee_score(experience_years, assigned_cases):
    if experience_years < 0:
        raise ValueError("Experience cannot be negative")

    if assigned_cases < 0:
        raise ValueError("Assigned cases cannot be negative")

    return experience_years * assigned_cases


class TestEmployeeScore(unittest.TestCase):

    def test_valid_score(self):
        result = calculate_employee_score(8, 12)
        self.assertEqual(result, 96)

    def test_negative_experience(self):
        with self.assertRaises(ValueError):
            calculate_employee_score(-1, 12)

    def test_negative_assigned_cases(self):
        with self.assertRaises(ValueError):
            calculate_employee_score(8, -1)


if __name__ == "__main__":
    unittest.main()