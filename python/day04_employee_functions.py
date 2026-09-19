import json


def load_employee_data():
    """Load and return employee data from the JSON file."""
    with open("employees.json", "r") as file:
        return json.load(file)


def validate_employee(employee):
    """Return True when an employee has all required fields."""
    required_fields = {"name", "department", "active", "assigned_cases"}

    if not isinstance(employee, dict):
        return False

    return required_fields.issubset(employee)


def count_active_employees(employees):
    """Return the number of active employees."""
    return sum(1 for employee in employees if employee.get("active", False))


def count_employees_by_department(employees):
    """Return the number of employees in each department."""
    employee_departments = {}

    for employee in employees:
        department = employee["department"]

        if department in employee_departments:
            employee_departments[department] += 1
        else:
            employee_departments[department] = 1

    return employee_departments


def calculate_total_cases(employees):
    """Return the total number of assigned cases."""
    return sum(employee["assigned_cases"] for employee in employees)


def build_employee_summary(employees):
    """Build and return a summary of employee data."""
    return {
        "total_employees": len(employees),
        "active_employees": count_active_employees(employees),
        "employees_by_department": count_employees_by_department(employees),
        "total_assigned_cases": calculate_total_cases(employees),
    }


def save_summary(summary):
    """Save the employee summary to a JSON file."""
    with open("employee_summary_day04.json", "w") as file:
        json.dump(summary, file, indent=4)


def main():
    # 1. Load employee data
    employees = load_employee_data()

    # 2. Validate employees
    for employee in employees:
        if not validate_employee(employee):
            print(f"Invalid employee: {employee}")

    # 3. Build summary
    summary = build_employee_summary(employees)

    # 4. Save summary
    save_summary(summary)

    # 5. Display results
    print(f"Total Employees: {summary['total_employees']}")
    print(f"Active Employees: {summary['active_employees']}")

    print("Employees by Department:")
    for department, count in summary["employees_by_department"].items():
        print(f"  {department}: {count}")

    print(f"Total Assigned Cases: {summary['total_assigned_cases']}")
    print("Summary saved successfully.")


if __name__ == "__main__":
    main()