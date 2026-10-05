from employee_utils import calculate_total_cases, calculate_experience

def main():
    experience = calculate_experience(2018, 2026)
    total_cases = calculate_total_cases(12, 9, 7)
    print(f"Experience: {experience}")
    print(f"Total Cases: {total_cases}")
if __name__ == "__main__":
    main()