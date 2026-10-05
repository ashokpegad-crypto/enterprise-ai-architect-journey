from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool

def employees_departments(employees):
    return {employee.employee_name : employee.department for employee in employees}
def active_employees_departments(employees):
    return {employee.employee_name : employee.department for employee in employees if employee.active}




employee1 = Employee("EMP001", "Ashok", "IT",  True)
employee2 = Employee("EMP002", "Ravi", "HR", False)
employee3 = Employee("EMP003", "Priya", "IT", True)

employees = [employee1, employee2, employee3]

print(f"Employee Departments: {employees_departments(employees)}")
print(f"Active Employee Departments: {active_employees_departments(employees)}")