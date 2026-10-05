class Employee:

    def __init__(self, employee_id, employee_name, department, role, active, location, experience_years, assigned_cases):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.role = role
        self.active = active
        self.location = location
        self.experience_years = experience_years
        self.assigned_cases = assigned_cases

    def is_active(self):
        return self.active

    def is_it_employee(self):
        return self.department == "IT"

    def is_high_workload(self):
        return self.assigned_cases >= 10

    def calculate_experience_label(self):
        return f"{self.experience_years} years"

employee1 = Employee("EMP001", "Ashok", "IT", "Pega Developer", True, "Bangalore", 8, 12)
employee2 = Employee("EMP002", "Ravi", "HR", "HR Specialist", False, "Hyderabad", 5, 4)

for employee in (employee1, employee2):
    print(f"Employee: {employee.employee_name}")
    print(f"Active: {employee.is_active()}")
    print(f"IT Employee: {employee.is_it_employee()}")
    print(f"High Workload: {employee.is_high_workload()}")
    print(f"Experience: {employee.calculate_experience_label()}")
    print()
