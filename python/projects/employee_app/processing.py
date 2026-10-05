def count_active_employees(employees):
    """Calculate and return active employees from emloyees JSON file"""
    return sum(1 for employee in employees if employee.get("active",False))
def count_inactive_employees(employees):
    """Calculate and return inactive employees from emloyees JSON file"""
    return len(employees) - count_active_employees(employees)
def count_employees_by_department(employees):
    """Calculate employee count, active count, and cases by department."""
    employees_department = {}
    for employee in employees:
        department = employee["department"]
        if department not in employees_department:
            employees_department[department] = {
                "employee_count": 0,
                "active_count": 0,
                "assigned_cases": 0
            }

        department_summary = employees_department[department]
        department_summary["employee_count"] += 1
        department_summary["active_count"] += int(employee.get("active", False))
        department_summary["assigned_cases"] += employee.get("assigned_cases", 0)
    return employees_department
def calculate_total_cases(employees):
    """calculate and return total assigned cases"""
    return sum(employee.get("assigned_cases", 0) for employee in employees)

def calcualte_avarage_experience(employees):
    """Calculate and return avarage experience of the employees"""
    return sum(employee.get("experience_years", 0) for employee in employees) / len(employees)

def fetch_high_workload_employees(employees):
    """find and return the high work load employees"""
    high_workload_employees = []
    for employee in employees:
        assigned_cases = employee["assigned_cases"]
        if assigned_cases >= 10:
            high_workload_employees.append(employee["employee_id"])
    return high_workload_employees