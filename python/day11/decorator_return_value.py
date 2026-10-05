def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before function")

        result = func(*args, **kwargs)

        print("After function")

        return result

    return wrapper
@my_decorator
def calculate_total(a, b):
    return a + b

result = calculate_total(10, 20)
print(f"Result: {result}")

@my_decorator
def build_employee_label(name, department):
    return f"{name} - {department}"
label = build_employee_label("Ashok", "Pega Developer")
print(f"Label: {label}")