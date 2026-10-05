def introduce_employee(name, department, role):
    """Return a short introduction for an employee."""
    return f"{name} works in {department} as a {role}."


def calculate_experience(joining_year, current_year=2026):
    """Return the employee's experience in years."""
    return current_year - joining_year


def calculate_total_cases(case1, case2, case3):
    """Return the total number of assigned cases."""
    return case1 + case2 + case3


def build_employee_summary(name, department, active):
    """Return an employee summary dictionary."""
    status = "Active" if active else "Inactive"

    return {
        "name": name,
        "department": department,
        "status": status
    }


def main():
    employee = introduce_employee(
        name="Ashok",
        department="IT",
        role="Pega Developer"
    )
    print(employee)

    experience = calculate_experience(2018)
    print(f"Experience with default year: {experience}")

    experience = calculate_experience(2018, current_year=2025)
    print(f"Experience with custom year: {experience}")

    total_cases = calculate_total_cases(12, 9, 7)
    print(f"Total cases: {total_cases}")

    employee_summary = build_employee_summary(
        name="Ashok",
        department="IT",
        active=True
    )
    print(f"Employee summary: {employee_summary}")


if __name__ == "__main__":
    main()