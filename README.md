# Enterprise AI Architect Journey

My journey from Pega Architect to Enterprise AI & Automation Architect.

## Objective

Build the technical skills required to design, build, debug, test, and architect enterprise AI systems outside of a single platform.

The learning path is project-first: learn a concept, build it, debug/break it, document it, explain it, and repeat.

## Learning Focus

- Python & Software Engineering
- APIs & integration engineering
- LLM Engineering
- Context Engineering
- RAG & Knowledge Systems
- Agentic AI
- MCP
- Production AI Engineering
- AI Security
- AI Evaluation
- Enterprise AI Architecture

## Progress

### Python / Engineering Foundation

- Day 1 — Python basics ✅
- Day 2 — Control flow and core data structures ✅
- Day 3 — Data processing ✅
- Day 4 — Functions / modular design ✅
- Day 5 — Modules, packages, imports, exceptions ✅
- Day 6 — Files, JSON, CSV, environment variables / integration ✅
- Day 7 — Integration practice and review ✅
- Day 8 — OOP: classes, inheritance, composition ✅
- Day 9 — Dataclasses, type hints, typing ✅
- Day 10 — Comprehensions, iterators, generators ✅
- Day 11 — Decorators and context managers ✅
- Day 12 — Logging, debugging, unit testing ✅
- Day 13 — REST API client library ✅

## Day 13 Outcome

Built a reusable typed REST API client against the JSONPlaceholder Todo API.

Key capabilities:

- GET requests
- HTTP status handling with raise_for_status()
- request headers
- query parameters
- POST with JSON request body
- JSON response parsing
- reusable TodoApiClient
- shared _get() HTTP helper
- typed Todo dataclass
- conversion from external API dictionaries to internal models
- single-resource and collection operations
- filtering Todos by user

Primary file:

```text
python/day13_api_client.py
```

## Repository Structure

```text
learning-notes/    - Learning notes and technical concepts
python/            - Python practice and exercises
ai-engineering/    - AI engineering experiments and components
architecture/      - Architecture diagrams and decisions
projects/          - Major portfolio projects
```

## Learning Principle

For new concepts, understand:

1. What the concept is
2. Why it is useful
3. How it works
4. Small examples / predictions
5. A focused exercise written independently
6. Code/output review
7. Documentation and Git milestone

Do not treat later roadmap topics as current-day requirements unless a real dependency requires it.


## Learning Notes

Daily learning notes:

- [Day 1 — Python Basics](learning-notes/day01-python-basics.md)
- [Day 2 — Python Control Flow](learning-notes/day02-python-control-flow.md)
- [Day 3 — Data Structures, JSON and Data Processing](learning-notes/day03-python-data-structures-json.md)
- [Day 4 — Functions, Scope and Processing Pipelines](learning-notes/day04-python-functions-pipelines.md)
- [Day 5 — Modules, Packages, Imports and Code Organization](learning-notes/day05-python-modules-packages.md)
- [Day 6 — Files, JSON, CSV and Configuration](learning-notes/day06-python-files-json-csv-config.md)
- [Day 7 — Integration and Review](learning-notes/day07-python-integration-review.md)
- [Day 8 — OOP](learning-notes/day08-python-oop.md)
- [Day 9 — Dataclasses, Type Hints and Typing](learning-notes/day09-python-dataclasses-typing.md)
- [Day 10 — Comprehensions, Iterators and Generators](learning-notes/day10-python-comprehensions-iterators-generators.md)
- [Day 11 — Decorators and Context Managers](learning-notes/day11-decorators-context-managers.md)
- [Day 12 — Logging, Debugging and Unit Testing](learning-notes/day12-python-logging-debugging-testing.md)
- [Day 13 — REST API Client Library](learning-notes/day13-rest-api-client.md)

## Next

- Day 14 — Review and refactor the API client; explain and defend the design decisions.
