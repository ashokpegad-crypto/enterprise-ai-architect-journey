# Day 3 — Python Data Structures, JSON and Data Processing

## Source review
The repository contains 24 Day 3 Python practice files. The notes below are based on the actual Day 3 source files, including list, tuple, set, dictionary, nested-data, JSON, filtering, summary, and error-handling exercises.

## Objective
Learn how Python stores and processes collections of related data, then move from in-memory structures to JSON files.

## Topics completed
- Lists and indexing
- List slicing
- Tuples and immutability
- Sets and set operations
- Dictionaries and dictionary iteration
- Safe dictionary access
- Nested dictionaries inside lists
- Filtering collections
- Counting and aggregation
- JSON strings vs Python objects
- json.loads() / json.dumps()
- json.load() / json.dump()
- JSON file error handling
- Building summaries from structured data

## Core mental model
Python data processing often follows:

Input collection → iterate → inspect fields → apply condition → calculate/aggregate → build result

## Lists
Lists are ordered, mutable collections. The Day 3 exercises used them to hold multiple customer/employee records.

Useful operations practiced:
- indexing: items[0]
- iteration: for item in items
- slicing: items[start:end]
- append(): add an item

## Tuples
Tuples are ordered collections that are not intended to be modified after creation. The Day 3 immutable-tuple exercise demonstrated the difference between a mutable list and an immutable tuple.

## Sets
Sets store unique values. They are useful when the goal is uniqueness rather than ordering.

The exercises used sets to determine unique customer types/departments and demonstrated set operations.

## Dictionaries
Dictionaries represent key/value data and are central to JSON-shaped application data.

Example shape:
customer = {"id": "CUST001", "name": "Ashok", "type": "Gold", "active": True}

Dictionary access used in the exercises:
- customer["name"]
- customer.get("active", False)
- iteration over dictionary items

Safe access matters when a key may not exist. get() lets the program provide a fallback instead of immediately raising KeyError.

## Nested data
The nested-data exercise stored multiple dictionaries inside a list:

customers → list → customer dictionary → fields

This is the same general shape returned by many APIs.

## JSON
JSON is a text/data interchange format. Python can convert between JSON and native Python structures.

Key operations practiced:
- json.loads(): JSON string → Python object
- json.dumps(): Python object → JSON string
- json.load(): JSON file → Python object
- json.dump(): Python object → JSON file

Important distinction:
Python dictionary/list → in-memory object
JSON → serialized representation

## Filtering
The Day 3 filtering exercise selected Gold customers by evaluating a dictionary field:

customer["customer_type"] == "Gold"

That introduced a reusable processing pattern:
source collection → condition → matching collection

## Aggregation and summary
The JSON summary exercise counted:
- total customers
- active customers
- inactive customers
- Gold customers
- unique customer types

It then built a summary dictionary and saved it as JSON.

## Error handling
The JSON error-handling exercise distinguished common failure categories:
- FileNotFoundError
- json.JSONDecodeError
- KeyError
- unexpected Exception

This established the idea that different failure causes should be handled deliberately rather than treated as one generic problem.

## Enterprise AI relevance
These data structures become the building blocks for AI applications:
- user requests and metadata are often dictionaries
- retrieved documents are often lists of dictionaries/objects
- JSON is used by APIs and model services
- sets help with deduplication and uniqueness
- filtering and aggregation support routing, validation, retrieval and reporting

## Key takeaways
1. Choose a list when order and mutation matter.
2. Use tuples when the collection should not be changed.
3. Use sets when uniqueness matters.
4. Use dictionaries for key/value records.
5. JSON is a serialized representation; Python objects are in-memory structures.
6. load/dump work with files; loads/dumps work with strings.
7. Filtering and aggregation are core data-processing patterns.
8. Error handling should distinguish missing files, malformed data and missing keys.

## Status
Day 3 COMPLETE ✅