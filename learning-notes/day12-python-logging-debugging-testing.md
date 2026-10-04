# Day 12 — Logging, Debugging and Unit Testing

## Source review
The repository contains 18 Day 12 Python files plus the final integrated test module. The source covers logging basics, module loggers, exception logging, file logging, terminal/Pdb debugging, VS Code debugging, unit tests, assertions, expected exceptions, setUp/tearDown, domain tests, processing tests, validation tests, logging tests and the final Employee processor.

## Objective
Add observability and automated verification so the Employee application can be diagnosed and changed with confidence.

## Logging
Logging records application events in a structured way that can be filtered, persisted and analyzed.

Main levels practiced:
- DEBUG
- INFO
- WARNING
- ERROR

The code moved from root-level logging calls to:
logger = logging.getLogger(__name__)

## logger.exception()
logger.error() records an error message.
logger.exception() is intended for an exception handler and includes exception/traceback information.

## Context-rich logging
The Employee logging exercise recorded employee ID and name, and logged warnings when assigned cases reached the high-workload threshold.

## File logging
The source configured:
- level
- filename
- append mode
- timestamped format

Example log structure:
timestamp level logger_name message

## Debugging
Debugging asks why a program produced an incorrect result or failed.

Core workflow:
reproduce → pause → inspect state → step → identify divergence → fix → retest

## Pdb
The source practiced:
- breakpoint()
- p variable
- n
- c

breakpoint() pauses execution; p inspects values; n moves to the next line; c continues execution.

## Traceback analysis
The traceback exercise showed how to read a call chain from the failing operation back through the callers.

Important principle:
Do not only read the exception name; trace where the invalid value entered the failing function.

## VS Code debugging
The source also used the VS Code debugger with breakpoints, Variables, Step Over and Continue.

## Unit testing
Python's unittest framework was used to automate expected behavior.

Core ideas:
- TestCase groups tests.
- assertions verify expected behavior.
- setUp prepares fresh state before each test.
- tearDown performs cleanup after each test.

## Assertions
assertEqual checks an actual value against an expected value.

assertTrue / assertFalse verify Boolean behavior.

assertRaises verifies that invalid input produces the expected exception.

## Arrange → Act → Assert
The tests follow a useful pattern:
Arrange → create known test data
Act → call the function
Assert → verify the result

## Testing the Employee domain
Domain methods such as active status, IT membership and high workload were tested independently.

## Testing processing functions
The suite tested active employee names and high-workload employee names against a known five-employee dataset.

## Testing validation
Invalid Employee data was tested for missing ID, negative experience and negative assigned cases.

## Testing logging
assertLogs captured logger output so logging behavior itself could be verified automatically.

## Final production-style Employee Processor
The final application combines:
Employee input → Validation → Processing → Logging → Reporting

The tests verify:
- valid employee passes
- invalid employee raises ValueError
- active employee names
- high-workload names
- summary totals
- processing start/completion logging

## Engineering lesson
Business logic should remain testable independently from I/O. This makes tests fast, deterministic and easier to diagnose.

## Enterprise AI relevance
The same practices will be essential in AI services:
- logging request/operation context
- tracing failures in RAG/agent pipelines
- debugging prompt/context transformations
- testing deterministic parsing and validation
- testing tool input/output handling
- protecting changes with regression tests

## Day 12 completion criteria
- module logger ✅
- INFO/WARNING/ERROR ✅
- exception logging ✅
- file logging ✅
- breakpoint and inspection ✅
- VS Code debugging ✅
- domain method tests ✅
- processing tests ✅
- validation failure tests ✅
- logging tests ✅
- integrated Employee processor ✅

## Status
Day 12 COMPLETE ✅