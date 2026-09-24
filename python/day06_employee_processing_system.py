import json
import csv
import os
APP_ENV = os.environ.get("APP_ENV")
OUTPUT_FILE = os.environ.get("OUTPUT_FILE")


def load_employee_data(file_path):
    """Load employee records from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def load_employees_data_csv(file_path):
    with open(file_path, "r") as file:
        return list(csv.DictReader(file))

def validate_and_convert_csv_employee(employee):
    """Validate and convert one CSV employee dictionary."""
    required_fields = {"employee_id", "employee_name", "department", "role", "active", "location", "experience_years", "assigned_cases", }
    if not isinstance(employee, dict):
        raise TypeError("Employee must be a dictionary.")

    for field in required_fields:
        if field not in employee:
            raise KeyError(f"Missing required field: {field}")
        
    active_value = employee["active"].strip().lower()
    if active_value not in {"true", "false"}:
        raise ValueError("Invalid active value; expected 'true' or 'false'.")

    assigned_cases = employee["assigned_cases"]
    if assigned_cases.strip() == "":
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
    
    return {
        "employee_id": employee["employee_id"],
        "employee_name": employee["employee_name"],
        "department": employee["department"],
        "role": employee["role"],
        "active": active_value == "true",
        "location": employee["location"],
        "experience_years": experience_years,
        "assigned_cases": assigned_cases,
    }
"""Processing data"""
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

def build_employee_summary(employees):
    """Build and return the employees data sommary"""
    return {
        "environment": APP_ENV,
        "total_employees": len(employees),
        "active_employees": count_active_employees(employees),
        "inactive_employees": len(employees) - count_active_employees(employees),
        "employees_by_department": count_employees_by_department(employees),
        "total_assigned_cases": calculate_total_cases(employees)
    }
def save_summary(summary, save_path):
    """Save Summary as JSON file"""
    with open(save_path, "w") as file:
        json.dump(summary, file, indent=4)

def main():
    
    try:
        file_path="employees.json"
        employees = load_employee_data(file_path)
    except FileNotFoundError:
        print(f"JSON loading failed: file not found. {file_path}")
        return
    except json.JSONDecodeError:
        print(f"JSON loading failed: invalid JSON. {file_path}")
        return
    else:
        print("JSON loaded successfully.")
    file_path_csv="employees.csv"
    try:
        csv_employees = load_employees_data_csv(file_path_csv)
    except FileNotFoundError:
        print(f"File loading failed: file not found. {file_path_csv}")
        return
    else:
        print("File loaded successfully.")
    try:
        csv_employees_converted = [
            validate_and_convert_csv_employee(employee)
            for employee in csv_employees
        ]
    except (KeyError, ValueError, TypeError) as error:
        print(f"Validation failed: {error}")
        return
    summary = build_employee_summary(employees)
    save_path = OUTPUT_FILE

    json_employee_ids = {employee["employee_id"] for employee in employees}
    csv_employee_ids = {employee["employee_id"] for employee in csv_employees_converted}
    employee_count_matches = len(csv_employees_converted) == len(employees)
    missing_in_csv = json_employee_ids - csv_employee_ids
    extra_in_csv = csv_employee_ids - json_employee_ids

    if not employee_count_matches or missing_in_csv or extra_in_csv:
        print("Source verification: Failed")
        if not employee_count_matches:
            print(
                f"Employee count mismatch: JSON={len(employees)}, "
                f"CSV={len(csv_employees)}"
            )
        if missing_in_csv:
            print(f"Missing from CSV: {sorted(missing_in_csv)}")
        if extra_in_csv:
            print(f"Extra in CSV: {sorted(extra_in_csv)}")
        return
        
    else:
        print("Source verification: PASSED")
    print("Employee details")
    print("----------------")
    print(f"Environment: {summary['environment']}")
    print(f"JSON employees: {summary['total_employees']}")
    print(f"CSV employees: {len(csv_employees_converted)}")
    print(f"Active Employees: {summary['active_employees']}")
    print(f"InActive Emploee: {summary['inactive_employees']}")
    print("Employees by Department:")

    employee_department = count_employees_by_department(employees)
    for department, count in employee_department.items():
        print(f"  {department}: {count}")
    print(f"Total Assigned Cases: {summary['total_assigned_cases']}")
    save_summary(summary, save_path)
    print(f"Summary saved successfully. {save_path}")


if __name__ == "__main__":
    main()