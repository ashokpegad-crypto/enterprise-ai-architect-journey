# Day 11 — Decorators and Context Managers

## Engineering Observations

### Type Hints Describe the Contract

The employee collection in the exercise is a tuple, while `process_employees`
only needs to iterate over its input. `Iterable[Employee]` describes that
requirement more accurately and allows lists, tuples, and other iterable
collections:

```python
from collections.abc import Iterable

def process_employees(employees: Iterable[Employee]) -> None:
    ...
```

Python does not enforce this annotation at runtime. A type hint documents the
expected interface and helps static analysis; it does not convert or validate
the value passed to the function.

### Separate Responsibilities as Projects Grow

Importing `Employee` and sample `employees` directly from the Day 10 exercise
is convenient for a learning pipeline. In a production project, separate
responsibilities into modules for the domain model, test or sample data,
processing logic, and the application entry point. This helps prevent imports
from triggering unrelated application behavior. The current exercise does not
need to be reorganized for this observation.