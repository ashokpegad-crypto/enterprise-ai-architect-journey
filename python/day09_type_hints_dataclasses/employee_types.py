class Employee:

    def __init__(self, employee_id: str, employee_name: str, department: str, role: str, active: bool, location: str, experience_years: int, assigned_cases: int) -> None:
        self.employee_id: str = employee_id
        self.employee_name: str = employee_name
        self.department: str = department
        self.role:str = role
        self.active: bool = active
        self.location: str = location
        self.experience_years: int = experience_years
        self.assigned_cases: int = assigned_cases

    def is_active(self) -> bool:
        return self.active

    def is_it_employee(self) -> bool:
        return self.department == "IT"

    def is_high_workload(self) -> bool:
        return self.assigned_cases >= 10

    def calculate_experience_label(self) -> str:
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
