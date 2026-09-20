def validate_employee(employee):
    """Return True when an employee has all required fields."""
    required_fields = {"employee_id", "employee_name", "department", "role", "active", "location", "experience_years", "assigned_cases"}
    if not isinstance(employee, dict):
        return False
    return required_fields.issubset(employee)

def validate_employees(employees):
    """Validate all employees and return the overall validation status."""
    for employee in employees:
        if not validate_employee(employee):
            return False
    return True
