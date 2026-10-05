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

    def is_active(self) -> bool:
        return self.active

    def is_it_employee(self) -> bool:
        return self.department == "IT"

    def is_high_workload(self) -> bool:
        return self.assigned_cases >= 10


class TestEmployeeDomain(unittest.TestCase):

    def setUp(self):
        self.ashok = Employee(
            "EMP001", "Ashok", "IT", True, 8, 12
        )

        self.ravi = Employee(
            "EMP002", "Ravi", "HR", False, 5, 4
        )

    def test_active_employee(self):
        self.assertTrue(self.ashok.is_active())

    def test_inactive_employee(self):
        self.assertFalse(self.ravi.is_active())

    def test_it_employee(self):
        self.assertTrue(self.ashok.is_it_employee())

    def test_non_it_employee(self):
        self.assertFalse(self.ravi.is_it_employee())

    def test_high_workload_employee(self):
        self.assertTrue(self.ashok.is_high_workload())

    def test_normal_workload_employee(self):
        self.assertFalse(self.ravi.is_high_workload())


if __name__ == "__main__":
    unittest.main()