from dataclasses import dataclass

@dataclass
class Employee:
        employee_id: str
        employee_name: str
        department: str
        active: bool
        experience_years: int
        assigned_cases: int

def calculate_employee_score(employee):
    return employee.experience_years * employee.assigned_cases


def process_employee(employee):
    return calculate_employee_score(employee)


employee = Employee("EMP001", "Ashok", "IT", True, 8, 12)

score = process_employee(employee)

print(score)