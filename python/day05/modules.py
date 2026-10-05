import employee_utils

def main():
    experience = employee_utils.calculate_experience(2018, 2026)
    total_cases = employee_utils.calculate_total_cases(12, 9, 7)
    employee_label = employee_utils.build_employee_label("Ashok", "IT")
    print(f"Experience: {experience}")
    print(f"Total Cases: {total_cases}")
    print(f"Employee: {employee_label}")
if __name__ == "__main__":
    main()