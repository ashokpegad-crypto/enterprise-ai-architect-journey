from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool


employee1 = Employee("EMP001", "Ashok", "IT",  True)
employee2 = Employee("EMP002", "Ravi", "HR", False)
employee3 = Employee("EMP003", "Priya", "IT", True)

employees = [employee1, employee2, employee3]
iterator = iter(employees)

print(next(iterator).employee_name)
print(next(iterator).employee_name)
print(next(iterator).employee_name)
print(next(iterator).employee_name)