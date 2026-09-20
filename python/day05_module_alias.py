import employee_utils as eu

def main():
    experience = eu.calculate_experience(2018, 2026)
    total_cases = eu.calculate_total_cases(12, 9, 7)
    employee_label = eu.build_employee_label("Ashok", "IT")
    print(f"Experience: {experience}")
    print(f"Total Cases: {total_cases}")
    print(f"Employee: {employee_label}")
if __name__ == "__main__":
    main()