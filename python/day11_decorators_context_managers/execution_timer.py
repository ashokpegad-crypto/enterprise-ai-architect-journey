import time


class ExecutionTimer:

    def __init__(self, operation_name):
        self.operation_name = operation_name

    def __enter__(self):
        print(f"Starting: {self.operation_name}")
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        elapsed = end_time - self.start_time

        print(f"Completed: {self.operation_name}")
        print(f"Elapsed time: {elapsed:.4f} seconds")

def process_employees():
    time.sleep(1)
    print("Processing employees")

with ExecutionTimer("employee processing"):
    process_employees()