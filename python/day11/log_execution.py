from functools import wraps


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Completed: {func.__name__}")

        return result

    return wrapper
@log_execution
def process_employees():
    print("Processing employees")
process_employees()

@log_execution
def calculate_total(a, b):
    return a + b
result = calculate_total(10, 20)
print(f"Result: {result}")