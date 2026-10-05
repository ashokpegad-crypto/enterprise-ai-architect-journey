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
        print("SETUP")
        self.employee = Employee(
            "EMP001",
            "Ashok",
            "IT",
            True,
            8,
            12
        )

    def tearDown(self):
        print("TEARDOWN")

    def test_employee_name(self):
        print("TEST NAME")
        self.assertEqual(self.employee.employee_name, "Ashok")

    def test_employee_department(self):
        print("TEST DEPARTMENT")
        self.assertEqual(self.employee.department, "IT")

if __name__ == "__main__":
     unittest.main()