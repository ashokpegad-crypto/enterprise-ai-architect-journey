import time
from contextlib import contextmanager


@contextmanager
def execution_timer(operation_name):
    print(f"Starting: {operation_name}")

    start_time = time.perf_counter()

    try:
        yield
    finally:
        elapsed = time.perf_counter() - start_time

        print(f"Completed: {operation_name}")
        print(f"Elapsed time: {elapsed:.4f} seconds")

def process_employees():
    time.sleep(1)
    print("Processing employees")


with execution_timer("employee processing"):
    print("Processing employees")
    raise ValueError("Processing failed")

