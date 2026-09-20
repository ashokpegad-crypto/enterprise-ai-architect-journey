import json

from .processing import (
    calculate_total_cases,
    count_active_employees,
    count_employees_by_department,
    count_inactive_employees
)


def build_employee_summary(employees):
    """Build and return the employees data sommary"""
    return {
        "total_employees": len(employees),
        "active_employees": count_active_employees(employees),
        "inactive_employees": count_inactive_employees(employees),
        "employees_by_department": count_employees_by_department(employees),
        "total_assigned_cases": calculate_total_cases(employees)
    }

def save_summary(summary, file_path):
    """Save Summary as JSON file"""
    with open(file_path, "w") as file:
        json.dump(summary, file, indent=4)