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


def get_active_employee_names(employees):
    return [
        employee.employee_name
        for employee in employees
        if employee.active
    ]


def get_high_workload_employee_names(employees):
    return [
        employee.employee_name
        for employee in employees
        if employee.assigned_cases >= 10
    ]


class TestEmployeeProcessing(unittest.TestCase):

    def setUp(self):
        self.employees = [
            Employee("EMP001", "Ashok", "IT", True, 8, 12),
            Employee("EMP002", "Ravi", "HR", False, 5, 4),
            Employee("EMP003", "Priya", "IT", True, 4, 9),
            Employee("EMP004", "Kiran", "Finance", True, 6, 15),
            Employee("EMP005", "Anil", "IT", False, 7, 11),
        ]

    def test_active_employee_names(self):
        result = get_active_employee_names(self.employees)

        self.assertEqual(
            result,
            ["Ashok", "Priya", "Kiran"]
        )

    def test_high_workload_employee_names(self):
        result = get_high_workload_employee_names(self.employees)

        self.assertEqual(
            result,
            ["Ashok", "Kiran", "Anil"]
        )


if __name__ == "__main__":
    unittest.main()