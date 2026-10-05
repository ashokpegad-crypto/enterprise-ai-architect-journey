from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool

def generate_employee_names(employees):
    for employee in employees:
        yield employee.employee_name

employee1 = Employee("EMP001", "Ashok", "IT",  True)
employee2 = Employee("EMP002", "Ravi", "HR", False)
employee3 = Employee("EMP003", "Priya", "IT", True)

employees = [employee1, employee2, employee3]
employees_generator = generate_employee_names(employees)

for employee_name in employees_generator:
    print(employee_name)
