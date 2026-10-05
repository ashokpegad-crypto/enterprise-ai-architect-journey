from dataclasses import dataclass
from typing import Optional

@dataclass
class Employee:
    employee_id: str
    email : Optional[str]
    phone : Optional[str]



employee1 = Employee("EMP001", "ashok@example.com", "9876543210")
employee2 = Employee("EMP002", None, "9123456780")


for employee in (employee1, employee2):
    print(f"Employee: {employee.employee_id}")
    print(f"Email: {employee.email}")
    print(f"Phone: {employee.phone}")
    print()
