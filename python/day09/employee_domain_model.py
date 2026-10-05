from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    role: str
    active: bool
    location: Optional[str]
    experience_years: int
    assigned_cases: int


def count_active_employees(employees: list[Employee]) -> int:
    return sum(1 for employee in employees if employee.active)
def count_employees_by_department(employees: list[Employee]) -> dict[str, int]:
    employees_department = {}
    for employee in employees:
        department = employee.department
        if department in employees_department:
            employees_department[department] += 1
        else:
            employees_department[department] = 1
    return employees_department
def get_employee_location(employee: Employee) -> str:
    """Return the employee location or a fallback when it is unavailable."""
    return employee.location or "Location not available"


employee1 = Employee("EMP001", "Ashok", "IT", "Pega Developer", True, "Bangalore", 8, 12)
employee2 = Employee("EMP002", "Ravi", "HR", "HR Specialist", False, "Hyderabad", 5, 4)
employee3 = Employee("EMP003", "Priya", "IT", "Python Developer", True, None, 4, 9)

employees = [employee1, employee2, employee3]

print(f"Active Employees: {count_active_employees(employees)}")
employee_department = count_employees_by_department(employees)
print(f"Departments: {employee_department}")
print(f"Ashok Location: {get_employee_location(employee1)}")
print(f"Ravi Location: {get_employee_location(employee2)}")
print(f"Priya Location: {get_employee_location(employee3)}")
