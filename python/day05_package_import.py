from employee_app import calculate_experience,calculate_total_cases,build_employee_label
def main():
    experience = calculate_experience(2018, 2026)
    total_cases =   calculate_total_cases(12, 9, 7)
    employee_label = build_employee_label("Ashok", "IT")
    print(f"Experience: {experience}")
    print(f"Total Cases: {total_cases}")
    print(f"Employee: {employee_label}")
if __name__ == "__main__":
    main()