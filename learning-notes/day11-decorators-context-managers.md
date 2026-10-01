# Day 11 — Decorators and Context Managers

## Source review
The repository contains 16 Day 11 Python files. The source covers functions as objects, nested functions, decorators, argument forwarding, return-value preservation, functools.wraps, logging decorators, class-based context managers, exception behavior, contextlib and an Employee processing pipeline.

## Objective
Learn how Python can wrap function behavior and manage resource/block lifecycles.

## Functions as objects
Functions can be stored in variables, passed as arguments and returned from other functions.

This enables higher-order behavior and is the foundation of decorators.

## Nested functions
A function can define another function inside it. The inner function can capture or use the surrounding context.

The source demonstrated nested validation and returned action functions.

## Decorators
A decorator receives a function and returns a replacement/wrapped function.

Core flow:
original function → decorator → wrapper → modified behavior

The @decorator syntax is a concise way to apply a decorator.

## Decorators with arguments
The source moved from wrapper() to:
wrapper(*args, **kwargs)

This allows a decorator to work with functions having different positional and keyword arguments.

## Returning values
The decorator stored the original result, executed the after behavior, and returned the result.

That preserved the caller contract.

## functools.wraps
@wraps(func) preserves useful metadata such as the original function name and docstring.

The exercise verified that the decorated function still reported the expected name and docstring.

## Practical log_execution decorator
The source created @log_execution to log function start and completion while returning the original result.

## Context managers
with controls a lifecycle around a block.

Conceptual flow:
enter → with block → exit/cleanup

## __enter__ and __exit__
The class-based context manager implemented both methods.

__exit__ is called even when the with block raises an exception.

The source inspected exc_type and exc_value to show exception information.

## Exception suppression
Returning True from __exit__ suppresses the exception. Returning False allows it to propagate.

## ExecutionTimer
The class-based ExecutionTimer used time.perf_counter() to measure elapsed time around a block.

## contextlib
@contextmanager provides a function-based way to create context managers using yield and cleanup logic.

The source used try/finally so elapsed-time reporting still occurs when an exception happens.

## Decorator vs context manager
Decorator → wraps function behavior.
Context manager → controls the lifecycle of a block/resource.

These solve different problems and should not be confused.

## Final Employee pipeline
The Day 11 pipeline combined @log_execution with an ExecutionTimer around Employee processing.

Flow:
Employee processing → decorator logs outer execution → timer measures inner block → processing/reporting

## Enterprise AI relevance
Decorators can later standardize behavior such as logging, tracing, validation or metrics around service calls.

Context managers can manage files, connections, transactions, temporary state and other lifecycles.

## Engineering observation
Importing an earlier script that contains top-level print statements can trigger those statements during import. Reusable modules should protect executable entry points with if __name__ == "__main__":.

## Status
Day 11 COMPLETE ✅