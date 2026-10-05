# Day 15 - HTTP Fundamentals

## Status

**COMPLETED**

Day 15 is the first dedicated HTTP fundamentals day in Week 3 - APIs.

### Roadmap target

- GET
- POST
- PUT
- DELETE
- Headers
- Status codes

Day 16 moves to REST API design. Authentication is Day 17. Python HTTP client patterns are Day 18. External API integration is Day 19. Timeout/retry/exponential backoff/rate-limit topics are Day 20. LLM Engineering begins later at Day 29.

---

## 1. Day 15 Objective

Build a clear mental model of an HTTP request and response, then use Python requests to work with:

- HTTP methods
- URL paths
- Query parameters
- Request headers
- JSON request bodies
- HTTP status codes
- Response JSON
- Basic HTTP error semantics

The focus was **HTTP fundamentals only**. Later roadmap topics were intentionally not pulled forward.

---

## 2. HTTP Request Anatomy

An HTTP request is a message sent from a client to a server to retrieve data or ask the server to perform an operation.

### Main parts

| Part | Meaning | Example |
|---|---|---|
| Method | Operation requested | GET / POST / PUT / DELETE |
| URL | Destination | https://httpbin.org/get |
| Path | Resource location | /todos/1 |
| Query parameters | Filtering/selection criteria | ?userId=1 |
| Headers | Request metadata/instructions | Accept: application/json |
| Body | Data sent with request | {"name":"Ashok"} |

### HTTP response

A response commonly contains:

- Status code
- Response headers
- Response body

### Mental model

~~~text
HTTP Request
    |
    +-- Method
    +-- URL
    |    +-- Path
    |    +-- Query parameters
    +-- Headers
    +-- Body (when needed)
    |
    v
  Server
    |
    v
HTTP Response
    |
    +-- Status code
    +-- Response headers
    +-- Response body
~~~

---

## 3. Exercise 1 - HTTP Request Anatomy

### File

python/day15_1_http_request_anatomy.py

### What was practiced

- GET request
- Query parameters through params
- Custom header through headers
- Reading response JSON
- Inspecting returned query parameters and headers

### Implementation

~~~python
import requests

params = {
    "employee_id": "EMP001",
    "department": "IT" }

headers = {
    "X-Employee-Client": "Day15"}

response = requests.get(
    "https://httpbin.org/get",
    params=params,
    headers=headers
)

data = response.json()

print(f"Status Code: {response.status_code}")
print(f"Request URL: {data['url']}")
print(f"Query params: {data['args']}")
print(f"Custom Header: {data['headers']['X-Employee-Client']}")
~~~

### Actual output

~~~text
Status Code: 200
Request URL: https://httpbin.org/get?employee_id=EMP001&department=IT
Query params: {'department': 'IT', 'employee_id': 'EMP001'}
Custom Header: Day15
~~~

### Review

**10/10**

The request successfully demonstrated URL construction, query parameters, custom headers, and response JSON inspection.

---

## 4. Exercise 2 - HTTP Methods

### File

python/day15_2_http_methods.py

### Core methods

| Method | Common purpose |
|---|---|
| GET | Retrieve data |
| POST | Create/submit data |
| PUT | Update/replace a resource |
| DELETE | Remove a resource |

### Implementation

~~~python
import requests

response1 = requests.get("https://httpbin.org/get")
print(f"GET Status: {response1.status_code}")
print(f"GET method: {response1.request.method}")

response2 = requests.post(
    "https://httpbin.org/post",
    json={"name": "Ashok", "department": "IT"}
)
print(f"POST Status: {response2.status_code}")
print(f"POST method: {response2.request.method}")

response3 = requests.put(
    "https://httpbin.org/put",
    json={"name": "Ashok", "department": "IT", "role": "Pega Developer"}
)
print(f"PUT Status: {response3.status_code}")
print(f"PUT method: {response3.request.method}")

response4 = requests.delete("https://httpbin.org/delete")
print(f"DELETE Status: {response4.status_code}")
print(f"DELETE method: {response4.request.method}")
~~~

### Actual output

~~~text
GET Status: 200
GET method: GET
POST Status: 200
POST method: POST
PUT Status: 200
PUT method: PUT
DELETE Status: 200
DELETE method: DELETE
~~~

### Review

**10/10**

All four methods were invoked successfully. Inspecting response.request.method was a valid verification technique.

---

## 5. Exercise 3 - HTTP Status Codes

### File

python/day15_3_http_status_codes.py

### Status-code groups

| Group | Meaning | Examples used |
|---|---|---|
| 1xx | Informational | Not directly exercised |
| 2xx | Success | 200, 201, 204 |
| 3xx | Redirection | Not directly exercised |
| 4xx | Client/request-related error | 400, 401, 403, 404 |
| 5xx | Server-side error | 500 |

### Implementation

~~~python
import requests

status_codes = [200, 201, 204, 400, 401, 403, 404, 500]

for code in status_codes:
    response = requests.get(f"https://httpbin.org/status/{code}")
    print(f"Status Requested: {code}")
    print(f"Status Received: {response.status_code}")
    print()
~~~

### Result

For every requested value, the received status matched the requested status.

### Review

**10/10**

The exercise established an important distinction: a 4xx or 5xx status is still an HTTP response. The server was reached and returned a response.

---

## 6. HTTP Error vs Connection Failure

This distinction was explicitly corrected during the final knowledge check.

| Situation | Meaning |
|---|---|
| 404 | Server responded; requested resource was not found |
| 500 | Server responded; internal server error |
| Connection failure | A usable HTTP response may never be received |

### Rule to remember

**HTTP error != network connection failure**

A 404 Not Found is an HTTP response error, not a network connection error.

---

## 7. Exercise 4 - HTTP Headers

### File

python/day15_4_http_headers.py

### Content-Type vs Accept

- **Content-Type** describes the format of the request body being sent.
- **Accept** communicates the response media type the client wants to receive.

### Implementation

~~~python
import requests

json_data = {
    "name": "Ashok",
    "department": "IT",
    "role": "Pega Developer"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(
    "https://httpbin.org/post",
    json=json_data,
    headers=headers
)

print(f"Status Code: {response.status_code}")

data = response.json()

print(f"Content-Type Header: {data['headers']['Content-Type']}")
print(f"Accept Header: {data['headers']['Accept']}")
print(f"Employee Name: {data['json']['name']}")
print(f"Department: {data['json']['department']}")
print(f"Role: {data['json']['role']}")
~~~

### Actual output

~~~text
Status Code: 200
Content-Type Header: application/json
Accept Header: application/json
Employee Name: Ashok
Department: IT
Role: Pega Developer
~~~

### Review

**10/10**

Request body, headers, and response JSON were all handled correctly.

---

## 8. Exercise 5 - Path Parameters vs Query Parameters

### File

python/day15_5_path_vs_query.py

### Examples

~~~text
/todos/1
/todos?userId=1
~~~

| URL shape | Meaning |
|---|---|
| /todos/1 | Target one specific Todo resource |
| /todos?userId=1 | Query/filter a collection |

### Implementation

~~~python
import requests

params = {
    "userId": "1"
}

response1 = requests.get(
    url="https://jsonplaceholder.typicode.com/todos/1"
)

print("Path Status Code:", response1.status_code)
print("Todo ID:", response1.json()['id'])
print("Todo Title:", response1.json()['title'])

response2 = requests.get(
    url="https://jsonplaceholder.typicode.com/todos",
    params=params
)

print("Query Status Code:", response2.status_code)
print("First Todo ID:", response2.json()[0]['id'])
print("Todos for User 1:", len(response2.json()))
~~~

### Actual output

~~~text
Path Status Code: 200
Todo ID: 1
Todo Title: delectus aut autem
Query Status Code: 200
First Todo ID: 1
Todos for User 1: 20
~~~

### Review

**10/10**

The exercise correctly demonstrated both resource identification and collection filtering.

### Minor style observation

response2.json() was called multiple times. A later refactor could cache it in a variable. This was only a code-quality observation and not a correctness issue.

---

## 9. REST-Oriented Decision to Carry Forward

### Specific resource -> path

Example:

~~~text
GET /employees/EMP001
~~~

This naturally identifies one employee resource.

### Collection filter -> query

Example:

~~~text
GET /employees?department=IT
~~~

This asks for a collection filtered by department.

The existence of future filters does not make query parameters preferable for every operation. Choose the URL shape according to the resource being addressed.

---

## 10. Exercise 6 - HTTP Fundamentals Integration

### File

python/day15_6_http_fundamentals_integration.py

### Objective

Combine all Day 15 fundamentals into one program:

- GET
- POST
- PUT
- DELETE
- query parameters
- custom headers
- Content-Type
- Accept
- JSON body
- status-code inspection
- response JSON extraction

### Integration map

| Operation | Endpoint | Main concepts |
|---|---|---|
| GET | https://httpbin.org/get | Query params + custom header |
| POST | https://httpbin.org/post | JSON body + Content-Type + Accept |
| PUT | https://httpbin.org/put | JSON body + updated role |
| DELETE | https://httpbin.org/delete | Method verification |

### Implementation

~~~python
import requests

params = {
    "employee_id": "EMP001",
    "department": "IT" }

headers = {
    "X-Employee-Client": "Day15"}

response = requests.get(
    "https://httpbin.org/get",
    params=params,
    headers=headers
)

data1 = response.json()

print("==Get Employee==")
print("Status Code:", response.status_code)
print("Employee ID:", data1['args']['employee_id'])
print("Department:", data1['args']['department'])
print("Client:", data1['headers']['X-Employee-Client'])

json_data = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "role": "Pega Developer"}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"}

response2 = requests.post(
    "https://httpbin.org/post",
    json=json_data,
    headers=headers
)

data2 = response2.json()

print("\n==Post Employee==")
print("Status Code:", response2.status_code)
print("Employee ID:", data2['json']['employee_id'])
print("Name:", data2['json']['name'])
print("Department:", data2['json']['department'])
print("Role:", data2['json']['role'])

json_data = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "role": "Senior Pega Developer"}

response3 = requests.put(
    "https://httpbin.org/put",
    json=json_data,
    headers=headers
)

data3 = response3.json()

print("\n==Put Employee==")
print("Status Code:", response3.status_code)
print("Employee ID:", data3['json']['employee_id'])
print("Role:", data3['json']['role'])

response4 = requests.delete("https://httpbin.org/delete")

print("\n==Delete Employee==")
print("Status Code:", response4.status_code)
print("Method:", response4.request.method)
~~~

### Actual output

~~~text
==Get Employee==
Status Code: 200
Employee ID: EMP001
Department: IT
Client: Day15

==Post Employee==
Status Code: 200
Employee ID: EMP001
Name: Ashok
Department: IT
Role: Pega Developer

==Put Employee==
Status Code: 200
Employee ID: EMP001
Role: Senior Pega Developer

==Delete Employee==
Status Code: 200
Method: DELETE
~~~

### Review

**10/10**

All required Day 15 concepts were integrated successfully.

No later roadmap topics were added to the exercise.

---

## 11. What Day 15 Added to the Python Foundation

| Existing foundation | Day 15 extension |
|---|---|
| Day 13 REST client | Deeper HTTP request/response reasoning |
| JSON parsing | Clear separation of request JSON and response JSON |
| Exception handling | HTTP status semantics |
| Query parameters | Path vs query design |
| External calls | Method/header/body combinations |

Day 15 therefore acts as the transport-level foundation for the REST API design work that follows.

---

## 12. raise_for_status()

From Day 13 and reinforced during the review:

~~~python
response.raise_for_status()
~~~

For successful responses, it does not raise an HTTP exception.

For 4xx or 5xx responses, it raises requests.exceptions.HTTPError.

### Mental model

~~~text
response.status_code
        |
        v
raise_for_status()
        |
        +-- 2xx -> continue
        |
        +-- 4xx/5xx -> HTTPError
~~~

---

## 13. Final Knowledge Check

### Score

**8.3 / 10**

### Strong areas

- Path vs query concept
- GET vs POST
- Status-code groups
- Content-Type vs Accept
- HTTP 500 meaning
- JSON request body
- Core HTTP mental model

### Corrections locked in

#### Q5 - 404

The initial answer treated 404 as a network connection error.

Correct model:

> 404 is an HTTP response error. The server was reached; the requested resource was not found.

#### Q10 - Specific employee endpoint

The initial answer preferred:

~~~text
GET /employees?employeeId=EMP001
~~~

because query parameters are useful for filtering.

Correct REST-oriented choice for a single identified employee:

~~~text
GET /employees/EMP001
~~~

Query parameters remain appropriate for collection queries:

~~~text
GET /employees?department=IT
~~~

---

## 14. Day 15 Definition of Done

Day 15 is complete when the learner can:

- explain an HTTP request
- identify method, URL, path, query parameters, headers, and body
- explain the corresponding response
- use GET, POST, PUT, and DELETE
- send JSON request bodies
- explain Content-Type and Accept
- interpret 2xx, 4xx, and 5xx status categories
- distinguish HTTP errors from connection failures
- explain path vs query parameters
- read response JSON
- integrate the concepts in one Python program

---

## 15. Explicitly Deferred Topics

These were intentionally not added to Day 15:

| Topic | Roadmap location |
|---|---|
| API keys / OAuth basics / JWT | Day 17 |
| Python HTTP client patterns | Day 18 |
| External API integration | Day 19 |
| Timeouts / retries / exponential backoff / rate limits | Day 20 |
| FastAPI | Week 4 / Day 22 onward |
| LLM Engineering | Day 29 onward |

This scope discipline keeps the roadmap sequence intact.

---

## 16. Day 16 Bridge

Day 15 answered:

> **How does an HTTP request and response work?**

Day 16 moves to:

> **How should we design a REST API?**

The next step is resource modeling, endpoint naming, collection vs individual resources, CRUD mapping, and request/response design.

---

## Final Status

**DAY 15 - COMPLETED**

The learner successfully completed six HTTP fundamentals exercises and passed the final knowledge check with a strong foundation.
