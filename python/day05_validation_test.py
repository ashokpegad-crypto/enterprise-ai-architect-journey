from employee_app.data_loader import load_employee_data
from employee_app.validation import validate_employee, validate_employees

def main():
    employees = load_employee_data("employees.json")
    if validate_employees(employees):
        print("All employees are valid: True")
    else:
        print("Employee validation failed.")
if __name__ == "__main__":
    main()