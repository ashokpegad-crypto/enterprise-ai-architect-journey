from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool
    role: str

def departments(employees):
    return {employee.department for employee in employees}
def active_employees_departments(employees):
    return {employee.department for employee in employees if employee.active}
def employee_roles(employees):
    return {employee.role for employee in employees}




employee1 = Employee("EMP001", "Ashok", "IT",  True, "Developer")
employee2 = Employee("EMP002", "Ravi", "HR", False, "Analyst")
employee3 = Employee("EMP003", "Priya", "IT", True, "Developer")

employees = [employee1, employee2, employee3]

print(f"All Departments: {departments(employees)}")
print(f"Active Employee Departments: {active_employees_departments(employees)}")
print(f"Employee Roles: {employee_roles(employees)}")