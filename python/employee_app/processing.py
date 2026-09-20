def count_active_employees(employees):
    """Calculate and return active employees from emloyees JSON file"""
    return sum(1 for employee in employees if employee.get("active",False))
def count_inactive_employees(employees):
    """Calculate and return inactive employees from emloyees JSON file"""
    return len(employees) - count_active_employees(employees)
def count_employees_by_department(employees):
    """Calculate and return active employees by the department"""
    employees_department = {}
    for employee in employees:
        department = employee["department"]
        if department in employees_department:
            employees_department[department] += 1
        else:
            employees_department[department] =1
    return employees_department
def calculate_total_cases(employees):
    """calculate and return total assigned cases"""
    return sum(employee.get("assigned_cases", 0) for employee in employees)