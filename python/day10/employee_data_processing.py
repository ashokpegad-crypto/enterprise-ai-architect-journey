from dataclasses import dataclass

@dataclass
class Employee:
        employee_id: str
        employee_name: str
        department: str
        active: bool
        experience_years: int
        assigned_cases: int

def heavy_workload_employees(employees):
      return [employee.employee_name for employee in employees if employee.assigned_cases >= 10]

def active_employee_cases(employees):
      return {employee.employee_name: employee.assigned_cases for employee in employees if employee.active}

def active_employees_department(employees):
       return {employee.department for employee in employees if employee.active}

def generate_high_workload_employees(employees):
    for employee in employees:
        if employee.assigned_cases >= 10:
            yield employee

def active_it_employees(employees):
       return (employee.employee_name for employee in employees if employee.active and employee.department == "IT")

employee1 = Employee("EMP001", "Ashok", "IT", True, 8, 12)
employee2 = Employee("EMP002", "Ravi", "HR", False, 5, 4)
employee3 = Employee("EMP003", "Priya", "IT", True, 4, 9)
employee4 = Employee("EMP004", "Kiran", "Finance", True, 6, 15)
employee5 = Employee("EMP005", "Anil", "IT", False, 7, 11)
employees = (employee1, employee2, employee3, employee4, employee5)

print(f"High Workload Employees: {heavy_workload_employees(employees)}")
print(f"Active Employees Cases: {active_employee_cases(employees)}")
print(f"Active Employees department: {active_employees_department(employees)}")
for employee in generate_high_workload_employees(employees):
    print(f"High Workload: {employee.employee_name} - {employee.assigned_cases}")
for employee_name in active_it_employees(employees):
    print(employee_name)