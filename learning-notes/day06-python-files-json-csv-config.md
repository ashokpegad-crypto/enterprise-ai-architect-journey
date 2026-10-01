# Day 6 — Files, JSON, CSV, Environment Variables and Integration

## Source review
The repository contains 8 Day 6 Python files. The source covers file loading, JSON errors, exception handling, raise, CSV generation/reading, CSV validation and environment-driven configuration.

## Objective
Work with real files and configuration, then integrate those skills into the Employee Data Processing System.

## Topics completed
- reading files
- JSON file loading
- CSV writing
- CSV reading
- JSON/CSV representation differences
- environment variables
- os.environ.get()
- configuration values
- required-field validation
- type conversion and normalization
- FileNotFoundError
- JSONDecodeError
- try / except / else / finally
- raise
- source verification

## File I/O
The project uses with open(...) so files are automatically closed after the block.

Core flow:
open → read/write → process → close

## JSON files
json.load(file) converts file contents into Python structures.

The exercises also demonstrated malformed JSON handling with json.JSONDecodeError.

## CSV
CSV data arrives as rows and fields represented as strings. The Day 6 code used csv.DictReader and csv.DictWriter.

Important difference:
JSON can preserve native JSON boolean/number representation; CSV fields are commonly read as strings and may need normalization.

## CSV normalization
The integration code converted:
- "true" / "false" → bool
- numeric strings → int

It also validated required fields before processing.

## Environment variables
The integration code reads configuration such as:
APP_ENV
OUTPUT_FILE

Environment variables allow configuration to change without modifying the application source.

## Exceptions
Day 6 practiced specific exception categories:
- FileNotFoundError for missing input
- JSONDecodeError for malformed JSON
- ValueError for invalid conversion
- KeyError for missing required fields
- TypeError for incorrect object types

## raise
raise is used when the program detects an invalid condition and needs to stop normal processing with a specific exception.

## Integrated Employee Data Processing System
The final integration connected JSON and CSV sources, validated/converted CSV records, checked source consistency and generated a summary.

Integration flow:
Configuration → JSON load → CSV load → CSV validation/conversion → source verification → processing → summary → output

## Source verification
The integration compared employee counts and employee IDs between JSON and CSV so that the application could detect missing or extra records.

## Enterprise AI relevance
AI systems also consume data from:
- JSON APIs
- CSV exports
- environment configuration
- files
- enterprise systems

These skills are directly relevant to document ingestion, configuration management, API payloads and preprocessing pipelines.

## Engineering observations
- Validate at the boundary.
- Normalize external representations before business logic uses them.
- Keep secrets/configuration outside source code.
- Treat missing files and malformed data as explicit failure modes.

## Status
Day 6 COMPLETE ✅