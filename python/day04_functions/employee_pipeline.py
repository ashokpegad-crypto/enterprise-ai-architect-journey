import json

def load_employee_data():
    """Load and return employees data from the JSON file"""
    with open("employees.json", "r") as file:
        return json.load(file)
def validate_employee(employee):
    """Return True when an employee has all required fields."""
    required_fields = {"employee_name", "department", "active", "assigned_cases"}
    if not isinstance(employee, dict):
        return False
    return required_fields.issubset(employee)
def validate_employees(employees):
    """Validate all employees and return the overall validation status."""
    for employee in employees:
        if not validate_employee(employee):
            print(f"Invalid employee: {employee}")
            return False
    return True

def count_active_employees(employees):
    """Count and return all active employees"""
    return sum(1 for employee in employees if employee.get("active", False))

def count_employees_by_department(employees):
    """Count and Return employees count by the department"""
    employees_department = {}
    for employee in employees:
        department = employee["department"]
        if department in employees_department:
            employees_department[department] += 1
        else:
            employees_department[department] = 1
    return employees_department


def calculate_total_cases(employees):
    """calculate and return total assigned cases"""
    return sum(employee.get("assigned_cases", 0) for employee in employees)

def build_employee_summary(employees):
    """Build and return the employees data sommary"""
    return {
        "total_employees": len(employees),
        "active_employees": count_active_employees(employees),
        "employees_by_department": count_employees_by_department(employees),
        "total_assigned_cases": calculate_total_cases(employees)
    }
def save_summary(summary):
    """Save Summary as JSON file"""
    with open("employee_summary_day04.json", "w") as file:
        json.dump(summary, file, indent=4)

def main():
    employees = load_employee_data()

    if validate_employees(employees):
        print("All employees are valid.")
    else:
        print("Employee validation failed.")
        return
    summary = build_employee_summary(employees)
    save_summary(summary)
    print(f"Total Employees: {summary['total_employees']}")
    print(f"Active Employees: {summary['active_employees']}")
    print("Employees by Department:")
    for department, count in summary["employees_by_department"].items():
        print(f"  {department}: {count}")
    print(f"Total Assigned Cases: {summary['total_assigned_cases']}")
    print("Summary saved successfully.")

if __name__ == "__main__":
    main()