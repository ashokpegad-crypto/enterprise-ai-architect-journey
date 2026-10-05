from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool
    experience_years: int
    assigned_cases: int


def calculate_employee_score(employees):
    scores = []

    for employee in employees:
        score = employee.experience_years * employee.assigned_cases
        scores.append(f"{employee.employee_name} -> {score}")

    return scores


employee1 = Employee("EMP001", "Ashok", "IT", True, 8, 12)
employee2 = Employee("EMP002", "Ravi", "HR", False, 5, 4)
employee3 = Employee("EMP003", "Priya", "IT", True, 4, 9)

employees = (employee1, employee2, employee3)

result = calculate_employee_score(employees)

for score in result:
    print(score)