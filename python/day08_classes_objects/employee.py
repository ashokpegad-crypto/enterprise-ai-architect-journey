class Employee:

    def __init__(self, employee_id, employee_name, department, laptop):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.laptop = laptop

    def build_employee_label(self):
        return f"{self.employee_id} - {self.employee_name} - {self.department}"

    def is_it_employee(self):
        return self.department == "IT"

    def get_laptop_model(self):
        return self.laptop.model


class Laptop:

    def __init__(self, model):
        self.model = model

class Manager(Employee):
    def __init__(self, employee_id, employee_name, department, laptop, manager_level):
           super().__init__(employee_id, employee_name, department, laptop)
           self.manager_level = manager_level

    def build_employee_label(self):
        return f"Manager - {self.employee_id} - {self.employee_name} - {self.department}"

    def get_management_level(self):
        return self.manager_level
laptop = Laptop("Thinkpad")
employee1 = Employee("EMP001", "Ashok", "IT", laptop)
employee2 = Employee("EMP002", "Ravi", "HR", laptop)
manager = Manager("EMP003", "Priya", "IT", laptop, "Senior Manager")
print(f"Employee 1: {employee1.build_employee_label()}")
print(f"Employee 2: {employee2.build_employee_label()}")
print(f"Employee 1 laptop: {employee1.get_laptop_model()}")
print(f"Employee 1 in IT: {employee1.is_it_employee()}")
print(f"Employee 2 in IT: {employee2.is_it_employee()}")
print(f"Manager: {manager.build_employee_label()}")
print(f"Management Level: {manager.get_management_level()}")
print(f"Manager in IT: {manager.is_it_employee()}")
