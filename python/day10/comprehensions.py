from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool

def all_employees_names(employees):
    return [employee.employee_name for employee in employees]
def active_employees(employees):
    return [employee.employee_name for employee in employees if employee.active]
def it_employees(employees):
    return [employee.employee_name for employee in employees if employee.department == "IT"]



employee1 = Employee("EMP001", "Ashok", "IT",  True)
employee2 = Employee("EMP002", "Ravi", "HR", False)
employee3 = Employee("EMP003", "Priya", "IT", True)

employees = [employee1, employee2, employee3]

print(f"All Employees: {all_employees_names(employees)}")
print(f"Active Employees: {active_employees(employees)}")
print(f"IT Employees: {it_employees(employees)}")