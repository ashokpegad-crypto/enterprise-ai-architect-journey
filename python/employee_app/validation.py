def validate_employee(employee):
    """Return True when an employee has all required fields."""
    required_fields = {"employee_id", "employee_name", "department", "role", "active", "location", "experience_years", "assigned_cases"}
    if not isinstance(employee, dict):
        raise TypeError("Employee must be a dictionary.")

    for field in required_fields:
        if field not in employee:
            raise KeyError(f"Missing required field: {field}")
        
    if not isinstance(employee["active"], bool):
        raise ValueError("Invalid active value; expected True or False.")
    
    assigned_cases = employee["assigned_cases"]
    if assigned_cases == "":
        raise ValueError("assigned_cases cannot be empty.")
    try:
        assigned_cases = int(assigned_cases)
    except ValueError as error:
        raise ValueError("assigned_cases must be a valid integer.") from error

    experience_years = employee["experience_years"]
    try:
        experience_years = int(experience_years)
    except ValueError as error:
        raise ValueError("experience_years must be a valid integer.") from error
    
    return True
