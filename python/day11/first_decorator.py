def greet():
    print("Hello from greet")


def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

decorated_greet = my_decorator(greet)
decorated_greet()