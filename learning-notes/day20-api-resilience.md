# Day 20 - API Resilience

## Status

**COMPLETED**

Day 20 covered the API resilience stage of the roadmap:

- Timeouts
- Retries
- Exponential backoff
- Rate limits

The day ended with a manual resilient-client integration that demonstrated different behavior for different failure modes.

---

## 1. Learning Focus

The learning sequence was intentionally incremental:

~~~text
Timeout
  ↓
Retry
  ↓
Exponential Backoff
  ↓
Rate Limit / Retry-After
  ↓
Integrated Resilient Client
~~~

The emphasis was on understanding the mechanics before introducing higher-level retry abstractions.

---

## 2. Exercise 1 - Request Timeout

### File

`python/day20_api_resilience/01_request_timeout.py`

### Objective

Demonstrate a successful request with a timeout and a deliberately slow request that exceeds its timeout.

### Key mechanics

~~~python
response1 = session.get(
    url="https://httpbin.org/get",
    timeout=5,
    params={"employee_id": "EMP001"}
)
response1.raise_for_status()
data1 = response1.json()

try:
    response2 = session.get(
        url="https://httpbin.org/delay/5",
        timeout=2
    )
    response2.raise_for_status()
except requests.exceptions.Timeout:
    print("Result: REQUEST TIMED OUT")
~~~

### Actual output

~~~text
=== FAST API CALL ===
Status: 200
Employee ID: EMP001
Result: SUCCESS

=== TIMEOUT API CALL ===
Result: REQUEST TIMED OUT
~~~

### Review

**10/10**

The implementation correctly distinguished a transport-level timeout from an HTTP error response.

---

## 3. Exercise 2 - Basic Retry

### File

`python/day20_api_resilience/02_basic_retry.py`

### Objective

Retry an HTTP 503 response up to three attempts, with retrying limited specifically to status 503.

### Key mechanics

~~~python
max_retries = 3

for attempt in range(1, max_retries + 1):
    response = session.get(url, timeout=timeout)

    if response.status_code == 503 and attempt < max_retries:
        print("Result: RETRYING")
        continue

    print("Result: FAILED")
~~~

### Actual output

~~~text
=== RETRY DEMONSTRATION ===
Attempt: 1
Status: 503
Result: RETRYING

Attempt: 2
Status: 503
Result: RETRYING

Attempt: 3
Status: 503
Result: FAILED
~~~

### Review

**10/10**

The retry decision and maximum-attempt boundary were implemented correctly.

---

## 4. Exercise 3 - Exponential Backoff

### File

`python/day20_api_resilience/03_exponential_backoff.py`

### Objective

Add a growing delay between retry attempts.

### Formula

~~~text
delay = base_delay * 2^(attempt - 1)
~~~

With a base delay of 1 second:

~~~text
Attempt 1 -> wait 1 second
Attempt 2 -> wait 2 seconds
Attempt 3 -> final failure; no additional sleep
~~~

### Key implementation

~~~python
delay = base_delay * 2 ** (attempt - 1)
time.sleep(delay)
~~~

### Actual output

~~~text
=== EXPONENTIAL BACKOFF ===
Attempt: 1
Status: 503
Waiting: 1 seconds
Result: RETRYING

Attempt: 2
Status: 503
Waiting: 2 seconds
Result: RETRYING

Attempt: 3
Status: 503
Result: FAILED
~~~

### Review

**10/10**

The backoff calculation and placement of the delay before the next attempt were correct.

---

## 5. Exercise 4 - Rate Limit Handling

### File

`python/day20_api_resilience/04_rate_limit_handling.py`

### Objective

Handle HTTP 429 and respect a server-provided Retry-After value in a controlled demonstration.

### Key mechanics

~~~python
if status_response.status_code == 429:
    retry_after = int(headers_response.headers["Retry-After"])
    time.sleep(retry_after)
~~~

### Actual output

~~~text
=== RATE LIMIT HANDLING ===
Status: 429
Retry-After: 3 seconds
Result: RATE LIMITED
~~~

### Review

**10/10**

The implementation correctly detected 429, read the Retry-After value, converted it to an integer, and waited.

### Controlled-test note

The demonstration used httpbin's status endpoint for 429 and a separate response-headers endpoint to supply Retry-After: 3. In a real rate-limited API, Retry-After would normally be read directly from the 429 response when the API supplies it.

---

## 6. Exercise 5 - Resilient API Client

### File

`python/day20_api_resilience/05_resilient_api_client.py`

### Objective

Combine normal success, 503 retry with exponential backoff, timeout handling, and 429 rate-limit handling into one flow.

### Integrated behavior

~~~text
Normal 200
  -> process response

503
  -> retry
  -> exponential backoff
  -> stop after configured attempts

Timeout
  -> catch Timeout exception

429
  -> read Retry-After
  -> wait
~~~

### Actual output

~~~text
=== NORMAL REQUEST ===
Status: 200
Employee ID: EMP001
Result: SUCCESS

=== SERVICE UNAVAILABLE ===
Attempt: 1
Status: 503
Waiting: 1 seconds
Result: RETRYING

Attempt: 2
Status: 503
Waiting: 2 seconds
Result: RETRYING

Attempt: 3
Status: 503
Result: FAILED

=== TIMEOUT ===
Result: REQUEST TIMED OUT

=== RATE LIMIT ===
Status: 429
Retry-After: 3 seconds
Result: RATE LIMITED
~~~

### Review

**10/10**

All four Day 20 resilience mechanisms were demonstrated together, with different behavior for different failure modes.

---

## 7. Failure Decision Model

| Condition | Meaning | Client behavior |
|---|---|---|
| Success | Operation completed | Process response |
| Timeout | Response did not arrive within configured timeout behavior | Handle Timeout |
| 503 | Service temporarily unavailable | Retry with bounded exponential backoff |
| 429 | Client is being rate limited | Respect Retry-After when supplied |
| 404 | Resource not found | Do not blindly retry |

The central lesson is:

> Resilience is not retrying everything. Resilience is choosing behavior appropriate to the failure mode.

---

## 8. Key Engineering Lessons

- External requests should have explicit timeout boundaries.
- Retries should be bounded.
- Not every HTTP error is retryable.
- Exponential backoff reduces repeated immediate traffic against an unhealthy service.
- Server-provided Retry-After guidance should be respected when available.
- Transport failures, HTTP failures, and rate limiting are different failure classes.
- Response validation should occur before assuming the expected business payload is available.

---

## 9. Scope Intentionally Deferred

The following were not pulled into Day 20:

- Jitter
- HTTPAdapter / urllib3 Retry
- Generic retry abstractions
- Async HTTP / httpx
- Production-specific rate-limit policy

These require additional context and are kept separate so the manual mechanics remain clear.

---

## 10. Day 20 Definition of Done

- Timeout configured and handled.
- Basic retry implemented.
- Retry count bounded.
- Exponential backoff implemented.
- 503 service-unavailable path handled.
- 429 rate-limit path handled.
- Retry-After read and respected.
- Integrated resilient client completed.
- All exercises independently implemented and reviewed.
- Final validation: **10/10**.

---

## 11. Roadmap Transition

~~~text
Day 15 -> HTTP Fundamentals
Day 16 -> REST API Design
Day 17 -> API Authentication
Day 18 -> Python HTTP Clients & API Integration
Day 19 -> External API Integration
Day 20 -> API Resilience
Day 21 -> Review
~~~

Day 20 closes the resilience portion of the API sequence. Day 21 is the consolidation review before moving forward.
