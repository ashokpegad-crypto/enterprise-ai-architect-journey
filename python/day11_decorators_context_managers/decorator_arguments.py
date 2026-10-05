def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before function")
        func(*args, **kwargs)
        print("After function")

    return wrapper
@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Ashok")

@my_decorator
def introduce(name, role):
    print(f"{name} is a {role}")

introduce("Ashok", "Pega Developer")