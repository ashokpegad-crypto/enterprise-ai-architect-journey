from contextlib import contextmanager


@contextmanager
def employee_processing_context():
    print("Entering employee processing")

    yield

    print("Exiting employee processing")

with employee_processing_context():
    print("Processing employees")
    raise ValueError("Something went wrong")