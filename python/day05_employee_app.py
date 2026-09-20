from employee_app import load_employee_data, count_employees_by_department, count_inactive_employees, count_active_employees, calculate_total_cases, build_employee_summary, validate_employee, validate_employees, save_summary

def main():
    employees = load_employee_data("employees.json")
    if validate_employees(employees):
        print("All employees are valid: True")
    else:
        print("Employee validation failed.")
        return
    print("\nEmployee Summary")
    print("----------------")
    print(f"Active Employees: {count_active_employees(employees)}")
    print("Employees by Department:")
    employee_department = count_employees_by_department(employees)
    for department, count in employee_department.items():
        print(f"  {department}: {count}")
    print(f"Total Assigned Cases: {calculate_total_cases(employees)}")
    summary = build_employee_summary(employees)
    save_summary(summary, "employees_day05.json")
    print("\nSummary saved successfully.")

if __name__ == "__main__":
    main()