class MyContext:

    def __enter__(self):
        print("Entering context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        print(f"Exception type: {exc_type}")
        print(f"Exception value: {exc_value}")

        return True

with MyContext():
    print("Inside context")
    raise ValueError("Something went wrong")
print("Program continued")