import os
from employee_app import load_employee_data, count_employees_by_department, build_employee_summary, validate_employee,build_employee_summary, save_summary

APP_ENV = os.environ.get("APP_ENV")
OUTPUT_FILE = os.environ.get("OUTPUT_FILE")
INPUT_FILE = os.environ.get("INPUT_FILE")

def main():
    try:
        file_path= INPUT_FILE
        employees = load_employee_data(file_path)
    except FileNotFoundError:
        print(f"JSON loading failed: file not found. {file_path}")
        return
    try:
        for employee in employees:
            validate_employee(employee)
    except (KeyError, ValueError, TypeError) as error:
        print(f"Validation failed: {error}")
        return
    summary = build_employee_summary(employees)
    print("\nEmployee Summary")
    print("----------------")
    print(f"Total Employees: {summary["total_employees"]}")
    print(f"Active Employees: {summary["active_employees"]}")
    print(f"In Active Employees: {summary["inactive_employees"]}")
    print(f"Total Assigned Cases: {summary["total_assigned_cases"]}")
    print(f"Avarage Experience: {summary["average_experience"]}")
    print("Employees by Department:")
    for department, department_summary in summary["departments"].items():
        print(f"  {department}: {department_summary}")
    print(f"High WorkLoad Employees: {summary["high_workload_employees"]}")
    save_summary(summary, OUTPUT_FILE)
    print("\nSummary saved successfully.")

if __name__ == "__main__":
    main()