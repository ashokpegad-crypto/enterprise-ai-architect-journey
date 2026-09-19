def create_employee():
    name = "Ashok"
    return name


def function_one():
    value = 100
    print(value)


def function_two():
    value = 200
    print(value)


def count_employees(employees):
    return len(employees)


def get_employee_count(employees):
    count = count_employees(employees)
    return f"Total employees: {count}"


def main():
    print(create_employee())

    function_one()
    function_two()

    employees = ["Ashok", "John", "David"]

    print(f"Employee Count: {count_employees(employees)}")
    print(get_employee_count(employees))


if __name__ == "__main__":
    main()