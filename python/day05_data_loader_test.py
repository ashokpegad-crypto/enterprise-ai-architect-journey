from employee_app.data_loader import load_employee_data

def main():
    employees = load_employee_data("employees.json")
    print(f"Employees: {employees}")
if __name__ == "__main__":
    main()