import json

from .processing import (
    calculate_total_cases,
    count_active_employees,
    count_employees_by_department,
    count_inactive_employees,
    calcualte_avarage_experience,
    fetch_high_workload_employees
)


def build_employee_summary(employees):
    """Build and return the employees data sommary"""
    return {
        "total_employees": len(employees),
        "active_employees": count_active_employees(employees),
        "inactive_employees": count_inactive_employees(employees),
        "total_assigned_cases": calculate_total_cases(employees),
        "average_experience": calcualte_avarage_experience(employees),
        "departments": count_employees_by_department(employees),
        "high_workload_employees": fetch_high_workload_employees(employees)
    }

def save_summary(summary, file_path):
    """Save Summary as JSON file"""
    with open(file_path, "w") as file:
        json.dump(summary, file, indent=4)