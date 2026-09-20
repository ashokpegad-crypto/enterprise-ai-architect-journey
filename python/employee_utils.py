def calculate_experience(joining_year, current_year):
    """Calculate and return experience of the employee"""
    return current_year - joining_year

def calculate_total_cases(case1, case2, case3):
    """Calculate and return the total number of cases."""
    return case1 + case2 + case3

def build_employee_label(name, department):
    """Build and retun employee label"""
    return f"{name} - {department}"