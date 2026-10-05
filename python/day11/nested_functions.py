def process_employee():

    def validate_employee():
        print("Validating employee")

    print("Starting employee processing")
    validate_employee()
    print("Employee processing completed")

def create_employee_action():

    def action():
        print("Employee action executed")

    return action

process_employee()
employee_action = create_employee_action()
employee_action()