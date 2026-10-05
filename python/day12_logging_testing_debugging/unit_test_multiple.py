import unittest

def calculate_employee_score(experience_years, assigned_cases):
    return experience_years * assigned_cases

class TestEmployeeScore(unittest.TestCase):

    def test_normal_cases(self):
        result = calculate_employee_score(8, 12)
        self.assertEqual(result, 96)

    def test_zero_cases(self):
        result = calculate_employee_score(8, 0)
        self.assertEqual(result, 0)

    def test_one_year_one_case(self):
        result = calculate_employee_score(1, 1)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()

    