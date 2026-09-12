# Day 1 — Python Basics

## What I Learned

Today I learned the basic building blocks of Python programming and created my first useful Python programs.

The topics I covered were:

- Variables
- Data types
  - `str`
  - `int`
  - `float`
  - `bool`
  - `None`
- `print()`
- `input()`
- Type conversion
- Arithmetic operators
- Comparison operators
- Logical operators
- Basic debugging
- Building an expense calculator

I also learned that Python treats values differently depending on their data type. This is important because incorrect data types can cause errors or unexpected results during calculations.

---

## 1. Variables

A variable is a name used to refer to a value.

Variables allow us to store information and use that information later in the program.

### Example

```python
name = "Ashok"
age = 35
experience = 12

print(name)
print(age)
print(experience)
```

### Output

```text
Ashok
35
12
```

### Explanation

In this example:

- `name` stores a string value.
- `age` stores an integer value.
- `experience` stores an integer value.
- The `=` operator assigns a value to a variable.

Python does not require us to declare the variable type separately.

The type is determined automatically from the assigned value.

---

## 2. Python Data Types

A data type defines the kind of value stored in a variable.

The basic data types practiced today were:

| Data Type | Meaning | Example |
|---|---|---|
| `str` | Text or string | `"Ashok"` |
| `int` | Whole number | `35` |
| `float` | Decimal number | `150000.50` |
| `bool` | Boolean value | `True` or `False` |
| `NoneType` | No value | `None` |

### Example

```python
name = "Ashok"
age = 35
experience = 12
salary = 150000.50
is_architect = True
manager = None

print(name)
print(age)
print(experience)
print(salary)
print(is_architect)
print(manager)

print(type(name))
print(type(age))
print(type(experience))
print(type(salary))
print(type(is_architect))
print(type(manager))
```

### Output

```text
Ashok
35
12
150000.5
True
None

<class 'str'>
<class 'int'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

### Important Learning

The `type()` function tells us the data type of a value.

For example:

```python
print(type("Ashok"))
print(type(35))
print(type(150000.50))
print(type(True))
print(type(None))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

---

## 3. The `print()` Function

The `print()` function displays information on the screen.

### Example

```python
print("Hello, Enterprise AI Architect!")
```

### Output

```text
Hello, Enterprise AI Architect!
```

We can print text, numbers, variables, and expressions.

### Example

```python
name = "Ashok"
age = 35

print(name)
print(age)
print(age + 5)
```

### Output

```text
Ashok
35
40
```

### Printing Multiple Values

```python
name = "Ashok"
experience = 12

print("Name:", name)
print("Experience:", experience)
```

### Output

```text
Name: Ashok
Experience: 12
```

---

## 4. The `input()` Function

The `input()` function is used to receive information from the user.

### Example

```python
name = input("Enter your name: ")

print("Hello", name)
```

### Example Output

```text
Enter your name: Ashok
Hello Ashok
```

### Important Learning

The `input()` function always returns the entered value as a string.

Even if the user enters a number, Python initially treats it as a `str`.

### Example

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

If the user enters:

```text
28
```

The output will be:

```text
28
<class 'str'>
```

Therefore, user input must usually be converted into the required data type before performing calculations.

---

## 5. Type Conversion

Type conversion means changing a value from one data type to another.

Common conversion functions are:

| Function | Converts Value To |
|---|---|
| `int()` | Integer |
| `float()` | Decimal number |
| `str()` | String |
| `bool()` | Boolean |

### Converting Input to an Integer

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
print(age + 5)
```

If the user enters:

```text
28
```

The output will be:

```text
28
<class 'int'>
33
```

### Converting Input to a Float

```python
salary = float(input("Enter your salary: "))

print(salary)
print(type(salary))
```

If the user enters:

```text
150000.50
```

The output will be:

```text
150000.5
<class 'float'>
```

### Converting an Integer to a String

```python
age = 35

age_text = str(age)

print(age_text)
print(type(age_text))
```

Output:

```text
35
<class 'str'>
```

### Important Learning

The following code causes an error:

```python
age = input("Enter your age: ")

print(age + 5)
```

Reason:

- `input()` returns a string.
- `5` is an integer.
- Python cannot directly add a string and an integer.

Correct version:

```python
age = int(input("Enter your age: "))

print(age + 5)
```

---

## 6. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor division | `17 // 5` | `3` |
| `%` | Modulus/remainder | `17 % 5` | `2` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Example

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### Output

```text
15
5
50
2.0
```

### Floor Division

```python
print(17 // 5)
```

Output:

```text
3
```

Floor division returns the whole-number portion of the division.

### Modulus

```python
print(17 % 5)
```

Output:

```text
2
```

The modulus operator returns the remainder.

### Exponentiation

```python
print(2 ** 3)
```

Output:

```text
8
```

This means:

```text
2 × 2 × 2 = 8
```

---

## 7. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `==` | Equal to |
| `!=` | Not equal to |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Example

```python
age = 28

print(age > 18)
print(age < 18)
print(age == 28)
print(age != 28)
print(age >= 28)
print(age <= 20)
```

### Output

```text
True
False
True
False
True
False
```

### Important Difference Between `=` and `==`

The `=` operator is used for assignment.

```python
age = 28
```

This assigns the value `28` to the variable `age`.

The `==` operator is used for comparison.

```python
age == 28
```

This checks whether `age` is equal to `28`.

It returns either `True` or `False`.

---

## 8. Logical Operators

Logical operators are used to combine or reverse conditions.

The main logical operators are:

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses the result |

### Example

```python
age = 28
experience = 12

print(age > 18 and experience > 5)
print(age > 30 and experience > 5)
print(age > 30 or experience > 5)
print(not age > 30)
```

### Output

```text
True
False
True
True
```

### Explanation

#### `and`

```python
age > 18 and experience > 5
```

Both conditions are true, so the result is:

```text
True
```

#### `or`

```python
age > 30 or experience > 5
```

The first condition is false, but the second condition is true.

Therefore, the result is:

```text
True
```

#### `not`

```python
not age > 30
```

The condition `age > 30` is false.

The `not` operator reverses it to:

```text
True
```

---

## 9. Basic Debugging Lessons

During Day 1, I practiced identifying and correcting simple Python errors.

### Debugging Lesson 1 — Incorrect Type Conversion

Incorrect code:

```python
age = int(type(age))
```

This is incorrect because `type(age)` returns a type object, not a value that should be converted into an integer.

Correct code:

```python
print(type(age))
```

### Debugging Lesson 2 — Input Returns a String

Incorrect code:

```python
income = input("Monthly income: ")
rent = input("Rent: ")

remaining = income - rent

print("Remaining:", remaining)
```

This causes a `TypeError`.

Reason:

- `income` is a string.
- `rent` is a string.
- Subtraction requires numeric values.

Correct code:

```python
income = int(input("Monthly income: "))
rent = int(input("Rent: "))

remaining = income - rent

print("Remaining:", remaining)
```

### Debugging Lesson 3 — String Concatenation

The following code joins strings together:

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

If the user enters:

```text
20000
20000
```

The output will be:

```text
2000020000
```

This happens because both values are strings, so `+` performs string concatenation.

Correct version:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

Output:

```text
40000
```

### Debugging Lesson 4 — Choosing `int()` or `float()`

Use `int()` when the input should be a whole number.

Example:

```python
age = int(input("Enter your age: "))
```

Use `float()` when the input may contain decimal values.

Example:

```python
salary = float(input("Enter your salary: "))
```

For financial values such as income and expenses, `float()` was used in the expense calculator so that decimal amounts can be accepted.

---

## 10. Mini-Project — Expense Calculator

### Objective

Create a Python program that:

1. Accepts monthly income.
2. Accepts different expense values.
3. Calculates total expenses.
4. Calculates remaining income.
5. Calculates the savings percentage.

### File

```text
python/expense_calculator.py
```

### Code

```python
income = float(input("Monthly income: "))

rent = float(input("Rent: "))

food = float(input("Food: "))

travel = float(input("Travel: "))

other = float(input("Other expenses: "))


total_expenses = rent + food + travel + other

remaining = income - total_expenses

savings_percentage = (
    (remaining / income) * 100
    if income != 0
    else 0
)


print(f"\nTotal expenses: ₹{total_expenses:,.2f}")

print(f"Remaining income: ₹{remaining:,.2f}")

print(f"Savings percentage: {savings_percentage:.2f}%")
```

### Example Input

```text
Monthly income: 146000
Rent: 2500
Food: 5000
Travel: 3000
Other expenses: 3000
```

### Example Output

```text
Total expenses: ₹13,500.00
Remaining income: ₹132,500.00
Savings percentage: 90.75%
```

### Formulas Used

#### Total Expenses

```text
Total expenses = Rent + Food + Travel + Other expenses
```

#### Remaining Income

```text
Remaining income = Monthly income - Total expenses
```

#### Savings Percentage

```text
Savings percentage = (Remaining income / Monthly income) × 100
```

### Important Code Concepts Used

#### `float()`

Used to accept decimal values:

```python
income = float(input("Monthly income: "))
```

#### Conditional Expression

Used to avoid division by zero:

```python
savings_percentage = (
    (remaining / income) * 100
    if income != 0
    else 0
)
```

If income is zero, the savings percentage is set to zero.

#### f-Strings

Used to format the output:

```python
print(f"Remaining income: ₹{remaining:,.2f}")
```

The formatting means:

- `₹` displays the currency symbol.
- `,` adds thousands separators.
- `.2f` displays two decimal places.

---

## 11. Expense Calculator Testing

I tested the expense calculator using different inputs.

### Test 1 — Normal Income and Expenses

Input:

```text
Income: 146000
Rent: 2500
Food: 5000
Travel: 3000
Other: 3000
```

Result:

```text
Total expenses: ₹13,500.00
Remaining income: ₹132,500.00
Savings percentage: 90.75%
```

Status:

```text
Passed
```

### Test 2 — Zero Income

Input:

```text
Income: 0
Expenses: 0
```

Result:

```text
Total expenses: ₹0.00
Remaining income: ₹0.00
Savings percentage: 0.00%
```

Status:

```text
Passed
```

The program did not crash because the code checks whether income is zero before dividing.

### Test 3 — Expenses Greater Than Income

Example:

```text
Income: 10000
Total expenses: 12000
```

Result:

```text
Remaining income: ₹-2,000.00
Savings percentage: -20.00%
```

This shows that expenses are greater than income.

The negative value is useful because it indicates a deficit.

### Test 4 — Invalid Input

Example input:

```text
-
```

Result:

```text
ValueError: could not convert string to float
```

This happened because `-` by itself is not a valid floating-point number.

### Learning from Testing

The program works for valid numeric input, but it does not yet handle invalid input gracefully.

A future improvement would be to use:

- `try`
- `except`
- Input validation
- Better error messages

These topics will be studied later.

---

## 12. Enterprise AI Relevance

Although these were basic Python concepts, they are important for future AI engineering work.

### Variables

Variables will store:

- User input
- API responses
- Configuration values
- Model names
- Token counts
- Retrieved documents
- Workflow results

### Data Types

AI applications frequently process:

- Strings from user prompts
- Integers such as token counts
- Floats such as confidence scores
- Booleans such as success flags
- `None` when a value is unavailable

### Input and Type Conversion

AI systems receive data from:

- Users
- APIs
- JSON payloads
- Databases
- Files
- External tools

Correct type conversion is important to avoid runtime errors.

### Conditions and Logical Operators

These will be used for:

- Validating user requests
- Checking API responses
- Deciding whether to call a tool
- Handling errors
- Routing requests to different models
- Controlling agent workflows

### Debugging

Debugging will become important when working with:

- LLM APIs
- RAG pipelines
- Vector databases
- MCP tools
- Agent workflows
- Production AI services

---

## 13. Key Takeaways

The main lessons from Day 1 were:

1. Variables store and reference values.
2. Python automatically determines variable types.
3. `type()` is used to inspect a value's data type.
4. `input()` always returns a string.
5. Numeric input must be converted using `int()` or `float()`.
6. Arithmetic operators perform calculations.
7. Comparison operators return `True` or `False`.
8. Logical operators combine conditions.
9. `=` is used for assignment.
10. `==` is used for equality comparison.
11. Incorrect data types can cause runtime errors.
12. Debugging requires understanding the expected data type.
13. f-strings help format readable output.
14. Conditional expressions can prevent division-by-zero errors.
15. Small programs are useful for practicing real programming concepts.

---

## 14. Files Created

The following files were created during Day 1:

```text
python/
├── day01_basics.py
├── day01_debug.py
└── expense_calculator.py
```

The learning notes were saved in:

```text
learning-notes/day01-python-basics.md
```

---

## 15. Day 1 Status

### Completed

- [x] Variables
- [x] Data types
- [x] `print()`
- [x] `input()`
- [x] Type conversion
- [x] Arithmetic operators
- [x] Comparison operators
- [x] Logical operators
- [x] Basic debugging
- [x] Expense calculator
- [x] Expense calculator testing
- [x] Learning notes documentation

### Not Yet Covered

The following topics were intentionally not studied in detail today:

- Conditional statements using `if` and `else`
- Loops
- Lists
- Dictionaries
- Functions
- Exception handling
- Classes and objects
- Advanced Python topics

These topics will be covered in later learning sessions.

---

## Day 1 Conclusion

Day 1 established the basic Python foundation required for the upcoming AI engineering journey.

I learned how to:

- Store values in variables.
- Understand different data types.
- Receive and convert user input.
- Perform calculations.
- Compare values.
- Combine conditions.
- Identify simple errors.
- Build and test a small Python application.

The most important lesson was:

> Always understand the data type before performing an operation.

This foundation will be useful when working with APIs, JSON, databases, LLM responses, RAG systems, and AI automation workflows.