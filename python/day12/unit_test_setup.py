import unittest
from dataclasses import dataclass

@dataclass
class Employee:
        employee_id: str
        employee_name: str
        department: str
        active: bool
        experience_years: int
        assigned_cases: int


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee("EMP001", "Ashok", "IT", True, 8, 12)
        self.employee2 = Employee("EMP002", "Ravi", "HR", False, 5, 4)
        self.employee3 = Employee("EMP003", "Priya", "IT", True, 4, 9)

    def test_employee_name(self):
        self.assertEqual(self.employee1.employee_name, "Ashok")

    def test_employee_department(self):
        self.assertEqual(self.employee2.department, "HR")

if __name__ == "__main__":
    unittest.main()