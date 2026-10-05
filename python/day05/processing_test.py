from employee_app.data_loader import load_employee_data
from employee_app.processing import count_active_employees,count_employees_by_department,calculate_total_cases

def main():
    employees = load_employee_data("employees.json")
    print(f"Active Employees: {count_active_employees(employees)}")
    print("Employees by Department:")
    employee_department = count_employees_by_department(employees)
    for department, count in employee_department.items():
        print(f"  {department}: {count}")
    print(f"Total Assigned Cases: {calculate_total_cases(employees)}")

if __name__ == "__main__":
    main()