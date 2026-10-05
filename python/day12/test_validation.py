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


def validate_employee(employee):
    if not employee.employee_id:
        raise ValueError("Employee ID is required")

    if not employee.employee_name:
        raise ValueError("Employee name is required")

    if employee.experience_years < 0:
        raise ValueError("Experience cannot be negative")

    if employee.assigned_cases < 0:
        raise ValueError("Assigned cases cannot be negative")

    return True

class TestEmployeeValidation(unittest.TestCase):

    def test_valid_employee(self):
        employee = Employee(
            "EMP001",
            "Ashok",
            "IT",
            True,
            8,
            12
        )

        self.assertTrue(validate_employee(employee))

    def test_negative_experience(self):
        employee = Employee(
            "EMP002",
            "Ravi",
            "HR",
            False,
            -1,
            4
        )

        with self.assertRaises(ValueError):
            validate_employee(employee)

    def test_negative_assigned_cases(self):
        employee = Employee(
            "EMP003",
            "Priya",
            "IT",
            True,
            4,
            -1
        )

        with self.assertRaises(ValueError):
            validate_employee(employee)

    def test_missing_employee_id(self):
        employee = Employee(
            "",
            "Kiran",
            "Finance",
            True,
            6,
            15
        )

        with self.assertRaises(ValueError):
            validate_employee(employee)

if __name__ == "__main__":
    unittest.main()