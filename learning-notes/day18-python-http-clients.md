# Day 18 - Python HTTP Clients

## Status

**COMPLETED**

Day 18 covered the Python HTTP client and API integration stage of Week 3.

### Roadmap target

- Python HTTP clients
- Reusable API client behavior
- API request/response integration

Day 17 covered authentication. Day 19 moves to external API integration, and Day 20 covers timeout/retry/exponential-backoff/rate-limit resilience.

---

## 1. Day 18 Learning Focus

Because the learner already has substantial REST integration experience in Pega, Day 18 minimized generic REST theory and focused on Python request mechanics and reusable client patterns:

- `requests.Session()`
- Session-level headers
- Request-level header override
- Reusable bearer authentication
- Query parameters with `params`
- JSON request bodies with `json=`
- Response parsing with `response.json()`
- HTTP response validation with `raise_for_status()`
- Handling `requests.exceptions.HTTPError`
- Combining GET + POST operations into one integration flow

---

## 2. HTTP Client Mental Model

~~~text
requests.Session()
      |
      +-- shared headers
      +-- reusable authentication
      +-- multiple HTTP requests
              |
              +-- GET /headers
              +-- GET /get
              +-- POST /post

Typical request flow:
request
  -> HTTP response
  -> raise_for_status()
  -> response.json()
  -> business data
~~~

A Session lets common client configuration be established once and reused across multiple HTTP requests.

A request-specific value can override a session default when a particular call needs different behavior.

---

## 3. Exercise 1 - requests.Session Fundamentals

### File

`python/day18_python_http_clients/01_requests_session.py`

### Objective

Create one Session, configure default headers once, make a request, then override one header for a specific request while preserving the other session-level default.

### Implementation

~~~python
import requests

session = requests.Session()

url = "https://httpbin.org/headers"
session.headers.update({
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"
})

response1 = session.get(url)
data = response1.json()
print("=== SESSION REQUEST 1 ===")
print(f"Status: {response1.status_code}")
print(f"Client: {data['headers']['X-Client-Name']}")
print(f"Accept: {data['headers']['Accept']}")

response2 = session.get(
    url,
    headers={"X-Client-Name": "employee-report-service"}
)
data2 = response2.json()
print("\n=== SESSION REQUEST 2 ===")
print(f"Status: {response2.status_code}")
print(f"Client: {data2['headers']['X-Client-Name']}")
print(f"Accept: {data2['headers']['Accept']}")
~~~

### Actual output

~~~text
=== SESSION REQUEST 1 ===
Status: 200
Client: enterprise-employee-service
Accept: application/json

=== SESSION REQUEST 2 ===
Status: 200
Client: employee-report-service
Accept: application/json
~~~

### Review

**10/10**

Demonstrated correctly:

- One reusable Session
- Session-level common headers
- Request-level header override
- Response values extracted from JSON

---

## 4. Exercise 2 - Authenticated Reusable Session

### File

`python/day18_python_http_clients/02_authenticated_session.py`

### Objective

Carry a bearer token and common client headers through one reusable Session, then use the same authenticated client against two different endpoints.

### Implementation

~~~python
import requests

session = requests.Session()
url = "https://httpbin.org/headers"
session.headers.update({
    "Authorization": "Bearer DAY17-DEMO-TOKEN",
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"
})

response1 = session.get(url)
data1 = response1.json()
print("=== EMPLOYEE API REQUEST ===")
print(f"Status: {response1.status_code}")
print(f"client: {data1['headers']['X-Client-Name']}")
print(f"Accept: {data1['headers']['Accept']}")

response2 = session.get(
    url="https://httpbin.org/get",
    params={"employee_id": "EMP001", "department": "IT"}
)
data2 = response2.json()
print("\n=== EMPLOYEE SEARCH REQUEST ===")
print(f"Status: {response2.status_code}")
print(f"Authentication Preset: {bool(data2['headers']['Authorization'])}")
print(f"Client: {data2['headers']['X-Client-Name']}")
print(f"Employee ID: {data2['args']['employee_id']}")
print(f"Department: {data2['args']['department']}")
~~~

### Actual output

~~~text
=== EMPLOYEE API REQUEST ===
Status: 200
client: enterprise-employee-service
Accept: application/json

=== EMPLOYEE SEARCH REQUEST ===
Status: 200
Authentication Preset: True
Client: enterprise-employee-service
Employee ID: EMP001
Department: IT
~~~

### Review

**9.8/10**

The implementation correctly demonstrated:

- Bearer Authorization at Session level
- Reuse of the same Session
- Multiple API endpoints
- Query parameters with `params`
- Authentication presence derived from the returned response

Minor note: `Authentication Preset` in the terminal output was a wording typo for `Authentication Present`. It did not affect the implementation.

---

## 5. Exercise 3 - Response Error Handling

### File

`python/day18_python_http_clients/03_response_error_handling.py`

### Objective

Validate a successful response and deliberately handle an HTTP 404 response using `raise_for_status()` and `requests.exceptions.HTTPError`.

### Implementation

~~~python
import requests

session = requests.Session()
url = "https://httpbin.org/get"
session.headers.update({
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"})

response = session.get(url, params={"employee_id": "EMP001"})
response.raise_for_status()
data = response.json()

print("=== SESSION API CALL ===")
print(f"Status: {response.status_code}")
print(f"Employee ID: {data['args']['employee_id']}")
print("Result: SUCCESS")

response2 = session.get(url="https://httpbin.org/status/404")
try:
    response2.raise_for_status()
except requests.exceptions.HTTPError:
    print("\n=== FAILED API CALL ===")
    print(f"Status: {response2.status_code}")
    print("Result: HTTP ERROR HANDLED")
~~~

### Actual output

~~~text
=== SESSION API CALL ===
Status: 200
Employee ID: EMP001
Result: SUCCESS

=== FAILED API CALL ===
Status: 404
Result: HTTP ERROR HANDLED
~~~

### Review

**10/10**

The important behavior was demonstrated:

~~~text
2xx response
  -> raise_for_status()
  -> no HTTPError
  -> continue processing

4xx/5xx response
  -> raise_for_status()
  -> HTTPError
  -> handle failure
~~~

Engineering refinement recorded during review: when the JSON payload is only meaningful after a successful HTTP operation, prefer:

~~~python
response.raise_for_status()
data = response.json()
~~~

This validates the HTTP operation before processing the expected business payload.

---

## 6. Exercise 4 - GET + POST Employee API Integration

### File

`python/day18_python_http_clients/04_employee_api_integration.py`

### Objective

Combine Session configuration, query parameters, JSON request bodies, response validation, and JSON extraction into one small API integration workflow.

### Implementation

~~~python
import requests

session = requests.Session()
url = "https://httpbin.org/get"
session.headers.update({
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"})

response = session.get(url, params={"employee_id": "EMP001"})
response.raise_for_status()
data = response.json()

json_data = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "role": "Pega Developer"
}

response2 = session.post(
    url="https://httpbin.org/post",
    json=json_data
)
employee_data = response2.json()
response2.raise_for_status()

print("=== GET EMPLOYEE ===")
print(f"Status: {response.status_code}")
print(f"Employee ID: {data['args']['employee_id']}")
print("\n=== CREATE EMPLOYEE ===")
print(f"Status: {response2.status_code}")
print(f"Employee ID: {employee_data['json']['employee_id']}")
print(f"Name: {employee_data['json']['name']}")
print(f"Department: {employee_data['json']['department']}")
print(f"Role: {employee_data['json']['role']}")
print("Result: SUCCESS")
~~~

### Actual output

~~~text
=== GET EMPLOYEE ===
Status: 200
Employee ID: EMP001

=== CREATE EMPLOYEE ===
Status: 200
Employee ID: EMP001
Name: Ashok
Department: IT
Role: Pega Developer
Result: SUCCESS
~~~

### Review

**10/10**

Demonstrated correctly:

- GET with query parameter
- `raise_for_status()`
- POST with `json=employee_data`
- JSON response extraction
- Complete GET + POST integration

Engineering refinement: in production code, prefer calling `response2.raise_for_status()` before `response2.json()` when the JSON is only meaningful after a successful HTTP response.

---

## 7. Day 18 Key Engineering Patterns

### Session-level configuration

Use one reusable Session when multiple API calls share client configuration such as common headers or authentication.

### Request-level override

A specific request can override a Session default when that call needs different behavior.

### Authenticated reusable client

A bearer access credential can be configured once at Session level and reused across multiple API calls.

### Query parameters

Use `params` for query-string inputs such as filters and search criteria.

Example:

~~~python
session.get(
    "https://httpbin.org/get",
    params={"employee_id": "EMP001", "department": "IT"}
)
~~~

### JSON request body

Use `json=` when sending application JSON.

Example:

~~~python
session.post(
    "https://httpbin.org/post",
    json=employee_data
)
~~~

### Response validation

Use `raise_for_status()` when a failed HTTP operation should become an exception rather than continue through the success path.

### Response parsing

Use `response.json()` to convert a JSON response into Python data structures that can be inspected and processed.

---

## 8. Combined Integration Model

~~~text
Enterprise-style Python API client

Create one reusable Session
        |
        v
Configure common headers / authentication
        |
        v
Call endpoint with params or JSON body
        |
        v
Validate HTTP response
        |
        v
Parse JSON payload
        |
        v
Extract business values
        |
        v
Continue to next API operation
~~~

This is the core bridge from individual Python HTTP calls to a reusable integration client.

---

## 9. Day 18 Validation

| Area | Evidence | Result |
|---|---|---|
| HTTP client creation | `requests.Session()` used in all exercises | Pass |
| Reusable configuration | Session headers reused across calls | Pass |
| Authentication reuse | Bearer token carried by Session | Pass |
| Query parameters | `params` used for employee_id / department | Pass |
| JSON integration | POST request sent with `json=` | Pass |
| Response parsing | `response.json()` used and values extracted | Pass |
| HTTP error handling | `raise_for_status()` + HTTPError handling | Pass |
| Combined integration | GET + POST employee workflow completed | Pass |

**Day 18 final status: COMPLETED.**

All four exercises were independently implemented and reviewed.

---

## 10. Important Lessons and Corrections

1. Use Session when multiple API calls share client configuration.
2. Keep authentication configuration separate from business request data.
3. Use `params` for query parameters and `json=` for JSON request bodies.
4. Use `raise_for_status()` when failed HTTP status should stop normal processing.
5. Validate the HTTP operation before assuming the response is the expected business payload.
6. Do not confuse an echo/test endpoint with a real API gateway, authorization server, or protected enterprise service.

---

## 11. Scope Intentionally Deferred

The following topics were deliberately not pulled into Day 18:

- Timeouts
- Retries
- Exponential backoff
- Rate limits
- HTTPAdapter / retry adapters
- Async HTTP / httpx
- FastAPI
- Database integration

Day 19 is the next external API integration stage. Day 20 is the resilience stage.

---

## 12. Test Endpoint Limitation

The exercises used `httpbin.org` as an echo/inspection service.

This means:

- The request was sent over HTTP successfully.
- Request headers and parameters could be inspected in the echoed response.
- JSON request bodies could be inspected in the echoed response.
- A 200 response did not prove that an API key or bearer token was valid.
- The protected endpoint did not perform enterprise authorization.
- The OAuth identity-provider scenario from Day 17 remained simulated.

The exercises therefore demonstrate Python HTTP client mechanics, not production identity or API gateway validation.

---

## 13. Day 18 Definition of Done

- `requests.Session()` understood and implemented.
- Session-level headers demonstrated.
- Per-request header override demonstrated.
- Bearer authentication reused through a Session.
- GET request with query parameters implemented.
- POST request with JSON body implemented.
- Successful HTTP response validation implemented.
- 404 HTTP error handling demonstrated.
- Combined GET + POST employee API integration completed.
- Learning captured in repository notes.

---

## 14. Next Roadmap Step

~~~text
Day 18
Python HTTP clients
      |
      v
Day 19
External API integration
      |
      v
Day 20
Timeouts + retries + backoff + rate limits
      |
      v
Day 21
Review
~~~

The Day 18 foundation is now:

**Reusable Session + authentication/common headers + request construction + response validation + JSON processing.**

The next step is to use these patterns against a meaningful external API integration rather than an echo service.
