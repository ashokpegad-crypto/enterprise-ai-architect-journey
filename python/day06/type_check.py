def check_employee_type(employee):
    
    if not isinstance(employee, dict):
        raise TypeError("Employee must be a dictionary.")
    return employee

def main():
    try:
        check_employee_type("EMP01")
    except TypeError as error:
        print(f"Type validation failed: {error}")
    else:
        print("Valid employee object")

if __name__ == "__main__":
    main()