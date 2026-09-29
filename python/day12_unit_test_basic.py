import unittest


def calculate_employee_score(experience_years, assigned_cases):
    return experience_years * assigned_cases


class TestEmployeeScore(unittest.TestCase):

    def test_calculate_employee_score(self):
        result = calculate_employee_score(8, 12)
        self.assertEqual(result, 96)


if __name__ == "__main__":
    unittest.main()