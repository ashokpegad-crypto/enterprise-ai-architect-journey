import unittest

from day12_employee_processor import (
    Employee,
    validate_employee,
    get_active_employee_names,
    get_high_workload_employee_names,
    build_employee_summary,
    process_employees,
    logger,
)


class TestEmployeeProcessor(unittest.TestCase):
    def setUp(self):
        self.employees = [
            Employee("EMP001", "Ashok", "IT", True, 8, 12),
            Employee("EMP002", "Ravi", "HR", False, 5, 4),
            Employee("EMP003", "Priya", "IT", True, 4, 9),
            Employee("EMP004", "Kiran", "Finance", True, 6, 15),
            Employee("EMP005", "Anil", "IT", False, 7, 11),
        ]

    def test_valid_employee(self):
        self.assertTrue(validate_employee(self.employees[0]))

    def test_invalid_employee(self):
        invalid_employee = Employee("EMP006", "Sita", "IT", True, -1, 5)

        with self.assertRaises(ValueError):
            validate_employee(invalid_employee)

    def test_active_employee_names(self):
        result = get_active_employee_names(self.employees)

        self.assertEqual(
            result,
            ["Ashok", "Priya", "Kiran"],
        )

    def test_high_workload_employee_names(self):
        result = get_high_workload_employee_names(self.employees)

        self.assertEqual(
            result,
            ["Ashok", "Kiran", "Anil"],
        )

    def test_employee_summary(self):
        result = build_employee_summary(self.employees)

        expected = (
            "Total Employees: 5\n"
            "Active Employees: 3\n"
            "High Workload Employees: 3"
        )

        self.assertEqual(result, expected)

    def test_processing_logging(self):
        with self.assertLogs(logger, level="INFO") as captured:
            process_employees(self.employees)

        self.assertTrue(
            any(
                "Employee processing started" in message
                for message in captured.output
            )
        )

        self.assertTrue(
            any(
                "Employee processing completed" in message
                for message in captured.output
            )
        )


if __name__ == "__main__":
    unittest.main()