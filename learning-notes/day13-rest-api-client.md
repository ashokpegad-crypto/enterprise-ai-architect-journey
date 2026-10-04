# Day 13 — REST API Client Library

## Roadmap outcome

Build a reusable Python API client library that calls an external REST API.

## Learning approach

New concepts were explained before exercises. The implementation was progressively refactored, with the learner writing the code independently.

## Core concepts

### REST request/response

Client → HTTP request → API → HTTP response → Client

Request concepts:
- method
- URL
- headers
- query parameters
- JSON body

Response concepts:
- status code
- headers
- response body

### GET and JSON

Used JSONPlaceholder Todo API:
`https://jsonplaceholder.typicode.com/todos/1`

Observed:
- status code 200
- JSON response
- field extraction

### HTTP status handling

Used `response.raise_for_status()` to turn unsuccessful 4xx/5xx responses into HTTP exceptions.

Demonstrated 404 handling with `requests.exceptions.HTTPError` and a try/except.

### Request headers

Used `headers={...}` and verified a custom header with httpbin.

### Query parameters

Used `params={...}` and verified returned query parameters in the httpbin `args` field.

### POST JSON body

Used `requests.post(..., json=data)` and inspected the returned `data` and parsed `json` sections.

## Reusable API client

Built:

```text
TodoApiClient
├── __init__(base_url)
├── _get(endpoint, params=None)
├── _to_todo(data)
├── get_todo(todo_id)
├── get_all_todos()
└── get_todos_by_user(user_id)
```

Responsibilities:
- `__init__`: store normalized base URL.
- `_get`: centralize URL building, GET, status checking, JSON parsing.
- public methods: express resource-specific operations.
- `_to_todo`: translate external JSON dictionaries into an internal model.

## Typed API model

```python
@dataclass
class Todo:
    user_id: int
    id: int
    title: str
    completed: bool
```

This creates a boundary:

External API JSON → client mapping → internal Todo model → application

The final client returns typed `Todo` objects instead of raw dictionaries.

## Final observed output

```text
Total Todos: 200
First Todo ID: 1
First Todo Title: delectus aut autem
First Todo Completed: False

Todos for User 1: 20
```

## Enterprise AI / LLM relevance

The same client boundary will later be used for LLM services, embeddings, enterprise APIs, and tools:

Python application
→ client
→ HTTP API
→ JSON response
→ typed/internal model
→ application logic

The key lesson is not merely how to call an API. It is how to isolate external communication and translate external data into a reusable internal abstraction.

## Scope discipline

Timeouts, retries, exponential backoff and rate limits were explored only as extra practice and are not treated as Day 13 core scope; they belong to later roadmap reliability work. Authentication is also a later topic.

## Exercise progression

1. Basic GET
2. status code and `raise_for_status()`
3. HTTPError handling
4. request headers
5. query parameters
6. POST with JSON
7. reusable client constructor
8. separate client responsibility from presentation
9. multiple resource operations
10. shared `_get()` helper
11. query parameters through shared helper
12. typed `Todo` model and API-to-model conversion

## Key takeaways

- `requests.get()` sends an HTTP GET request.
- `response.status_code` exposes the HTTP status.
- `raise_for_status()` turns unsuccessful HTTP responses into exceptions.
- `response.json()` parses JSON into Python data.
- headers carry request metadata.
- `params` sends query parameters.
- `json=` sends a JSON request body.
- a client class encapsulates external API communication.
- a shared helper prevents duplicated transport logic.
- dataclass models create a typed internal boundary.
- public client methods should describe capabilities; application code should handle presentation.

## Day 13 completion

**COMPLETE**

The roadmap Day 13 target is a reusable REST API client library, and the final implementation demonstrates that outcome.

## Knowledge Check — Questions and Answers

1. What is a REST API?
An HTTP-based interface that lets applications communicate with resources using methods such as GET and POST and structured data such as JSON.

2. What does requests.get() do?
It sends an HTTP GET request and returns a Requests Response object.

3. What is response.status_code?
The HTTP status code returned by the server, such as 200 or 404.

4. Why use raise_for_status()?
It raises a Requests HTTP exception for unsuccessful HTTP responses so failures are not silently treated as successful data.

5. What does response.json() do?
It parses a JSON response body into Python data such as a dictionary or list.

6. Headers vs query parameters?
Headers carry request metadata. Query parameters are values sent in the URL query string, typically for filtering or selection.

7. What does json=data mean in a POST?
It sends the supplied Python data as a JSON request body.

8. Why create TodoApiClient?
To encapsulate API communication in a reusable component rather than scattering HTTP code through application logic.

9. Why is _get() useful?
It centralizes common GET behavior such as URL building, request execution, status checking, and JSON parsing.

10. Why create the Todo dataclass?
To give the application a typed internal representation instead of passing raw external dictionaries through the system.

11. Why convert the API dictionary into a Todo object?
It creates a clear boundary between the external API schema and the internal application model.

12. get_todo() vs get_all_todos()?
The first retrieves one resource; the second retrieves a collection.

13. Why does get_todos_by_user() use params?
Because the API uses userId as a query parameter to filter the Todo collection.

14. Explain API → JSON → _to_todo() → Todo → Application.
The API returns external JSON, the client parses it, _to_todo() translates it into the internal dataclass, and the application uses that typed object.

15. Why is this useful for a future LLM client?
An LLM client follows the same boundary: build a request, call an external service, validate the response, parse JSON, translate the external response into an internal representation, and return usable data to application logic.

## Day 14 bridge

Next: review and refactor.

Focus areas:
- explain the complete API request/response lifecycle
- explain client vs application responsibilities
- defend the _get() abstraction
- explain external schema vs internal model
- identify production improvements without adding out-of-scope reliability/authentication features
- explain the design without relying on tutorial code
