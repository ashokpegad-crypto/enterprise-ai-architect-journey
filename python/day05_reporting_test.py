from employee_app.reporting import build_employee_summary,save_summary
from employee_app.data_loader import load_employee_data

def main():
    employees = load_employee_data("employees.json")
    summary = build_employee_summary(employees)
    print(summary)
    save_summary(summary, "employees_day05.json")
    print(f"Summary saved successfully.")
if __name__ == "__main__":
    main()