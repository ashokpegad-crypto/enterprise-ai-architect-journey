# Day 9 — Type Hints, Dataclasses and Typed Domain Models

## Source review
The repository contains 5 Day 9 Python files. The source demonstrates traditional classes with annotations, dataclasses, typed collections and Optional fields.

## Objective
Make the Employee domain model clearer and safer to use by documenting expected types and reducing constructor boilerplate.

## Topics completed
- type hints
- parameter annotations
- return annotations
- attribute annotations
- list[T]
- dict[K, V]
- Optional[T]
- dataclasses
- typed domain models
- None handling

## Type hints
Type hints describe the intended contract of code.

Example:
def count_active_employees(employees: list[Employee]) -> int:

Important: type hints do not automatically convert or validate values at runtime.

## Dataclasses
@dataclass generates common object boilerplate such as an initializer and a useful representation.

The Day 9 Employee dataclass retained domain methods while eliminating repetitive __init__ code.

## Typed collections
The code used:
- list[Employee]
- dict[str, int]

These communicate what kind of elements a function expects and returns.

## Optional
Optional[str] means a value may be a string or None.

The exercise modeled contact details and an employee location that could be unavailable.

## None and fallback behavior
The final domain model used:
employee.location or "Location not available"

This demonstrated a clean way to provide a fallback when an optional value is absent.

## Final Employee domain model
The final model contains:
- employee_id
- employee_name
- department
- role
- active
- location
- experience_years
- assigned_cases

Typed processing functions included:
- count_active_employees()
- count_employees_by_department()
- get_employee_location()

## Engineering lesson
Types document assumptions at the boundary of a function or model. They improve readability, editor support and static analysis even though Python itself remains dynamically typed.

## Enterprise AI relevance
Typed models become particularly useful for:
- API responses
- LLM structured output
- tool inputs/outputs
- retrieval metadata
- configuration
- workflow state

Day 13 reused this exact idea by converting an external JSON API response into a typed Todo dataclass.

## Status
Day 9 COMPLETE ✅