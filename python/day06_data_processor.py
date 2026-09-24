import json
import csv
import os
APP_ENV = os.environ.get("APP_ENV")
OUTPUT_FILE = os.environ.get("OUTPUT_FILE")


def load_employee_data(file_path):
    """Load employee records from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def prepare_employee_rows(employees):
    """Return the fields required by the CSV export."""
    fields = (
        "employee_id",
        "employee_name",
        "department",
        "role",
        "active",
        "location",
        "experience_years",
        "assigned_cases",
    )
    return [{field: employee.get(field) for field in fields} for employee in employees]

def save_employee_csv(employees, file_path):
    with open(file_path, "w", newline="") as file:
        fieldnames = employees[0].keys() if employees else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)

def load_employees_data_csv(file_path):
    with open(file_path, "r") as file:
        return list(csv.DictReader(file))

def validate_and_convert_csv_employee(first_employee):
    """Validate and convert one CSV employee dictionary."""
    required_fields = {"employee_id", "employee_name", "department", "role", "active", "location", "experience_years", "assigned_cases", }
    if not  isinstance(first_employee, dict):
        raise TypeError("Employee must be a dictionary.")

    for field in required_fields:
        if field not in first_employee:
            raise KeyError(f"Missing required field: {field}")
        

    active_value = first_employee["active"].strip().lower()
    if active_value not in {"true", "false"}:
        raise ValueError("Invalid active value; expected 'true' or 'false'.")

    assigned_cases = first_employee["assigned_cases"]
    if assigned_cases.strip() == "":
        raise ValueError("assigned_cases cannot be empty.")
    try:
        assigned_cases = int(assigned_cases)
    except ValueError as error:
        raise ValueError("assigned_cases must be a valid integer.") from error

    experience_years = first_employee["experience_years"]  
    try:
        experience_years = int(experience_years)
    except ValueError as error:
        raise ValueError("experience_years must be a valid integer.")
    
    return {
        "employee_id": first_employee["employee_id"],
        "employee_name": first_employee["employee_name"],
        "department": first_employee["department"],
        "role": first_employee["role"],
        "active": active_value == "true",
        "location": first_employee["location"],
        "experience_years": experience_years,
        "assigned_cases": assigned_cases,
    }


def main():
    employees = load_employee_data("employees.json")
    employee_rows = prepare_employee_rows(employees)
    save_employee_csv(employee_rows, "employees.csv")
    csv_employees = load_employees_data_csv("employees.csv")
    try:
        csv_employee_input = csv_employees[0].copy()
        csv_employee = validate_and_convert_csv_employee(csv_employee_input)
    except (KeyError, ValueError, TypeError) as error:
        print(f"Validation failed: {error}")
        return
    print(f"Environment: {APP_ENV}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"JSON employees: {len(employees)}")
    print(f"CSV employees: {len(csv_employees)}")
    print("Validated Employee Details:")
    print("---------------------------")
    print(f"Employee: {csv_employee["employee_id"]}")
    print(f"Active: {csv_employee["active"]}")
    print(f"Active type: {type(csv_employee["active"])}")
    print(f"Experience: {csv_employee["experience_years"]}")
    print(f"Experience type: {type(csv_employee["experience_years"])}")
    print(f"Cases: {csv_employee["assigned_cases"]}")
    print(f"Cases type: {type(csv_employee["assigned_cases"])}")

if __name__ == "__main__":
    main()