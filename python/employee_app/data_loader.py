import json


def load_employee_data(file_path):
    """Load and return employee data from the specified JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)