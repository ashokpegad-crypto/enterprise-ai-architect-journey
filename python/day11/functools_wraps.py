from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
@my_decorator
def greet(name):
    """Greet an employee."""
    print(f"Hello {name}")

print(greet.__name__)
print(greet.__doc__)