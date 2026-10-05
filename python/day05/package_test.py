from employee_app.calculations import calculate_experience,calculate_total_cases
from employee_app.formatting import build_employee_label

def main():
    experience = calculate_experience(2018, 2026)
    total_caseS = calculate_total_cases(12, 9, 7)
    employee_label = build_employee_label("Ashok", "IT")
    print(f"Experience: {experience}")
    print(f"Total cases: {total_caseS}")
    print(f"Employee: {employee_label}")
if __name__ == "__main__":
    main()