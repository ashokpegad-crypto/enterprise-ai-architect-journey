def validate_required_fields(employee):
    required_fields = ("employee_id", "employee_name", "department",)
    for field in required_fields:
        if field not in employee:
            raise KeyError(f"Missing required field: {field}")
    return True
def main():
    employee = {
    "employee_id": "EMP001",
    "employee_name": "Ashok"
}
    try:
        validate_required_fields(employee)
    except KeyError as error:
        print(f"Field validation failed: {error}")
    else:
        print(validate_required_fields(employee))

if __name__ == "__main__":
    main()