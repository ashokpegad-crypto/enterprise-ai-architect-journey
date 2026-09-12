# Day 2 — Python Control Flow

## Objective

Learn how to control program execution using conditions, logical operators,
nested conditions, loops, and input validation.

## Topics Completed

- if
- elif
- else
- Nested conditions
- and
- or
- not
- Boolean values
- String comparison
- while loops
- Input validation
- f-strings
- Business-rule implementation

## 1. Basic if/else

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

2. Multiple Conditions with elif
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 40:
    print("Grade: D")
else:
    print("Grade: F")
3. Logical Operators
and

All conditions must be true.

if has_experience and has_python_skill:
    print("Candidate is ready.")
or

At least one condition must be true.

if has_pega_experience or has_python_experience:
    print("Candidate has relevant experience.")
not

Reverses a Boolean value.

if not is_available:
    print("Candidate is unavailable.")
4. Nested Conditions

A condition inside another condition is called a nested condition.

if has_experience:
    if has_python_skill:
        print("Candidate meets the requirements.")

Nested conditions should be used carefully because too much nesting can make code difficult to read.

5. Cleaner Business Rules

Instead of deeply nested conditions:

if has_experience:
    if has_python_skill:
        if has_api_skill:
            print("Ready")

Use logical operators:

if has_experience and has_python_skill and has_api_skill:
    print("Ready")
6. Input Normalization

.lower() converts text to lowercase.

answer = input("Enter yes or no: ").lower()

.strip() removes extra spaces at the beginning and end.

answer = input("Enter yes or no: ").strip().lower()
7. Input Validation with while
answer = input("Enter yes or no: ").strip().lower()

while answer not in ("yes", "no"):
    print("Invalid input. Please enter yes or no.")
    answer = input("Enter yes or no: ").strip().lower()

The loop continues until the user provides an accepted value.

8. Practical Project

Created:

python/day02_candidate_eligibility.py

The program checks:

Candidate name

Years of experience

Python skill

API skill

Business Rules

At least 2 years of experience is required.

Python and API skills make the candidate fully eligible.

Relevant experience with only one skill means additional development is needed.

Otherwise, the candidate is not currently eligible.

Invalid yes/no input is rejected and requested again.