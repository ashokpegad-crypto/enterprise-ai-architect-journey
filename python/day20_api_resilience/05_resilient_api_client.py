import requests
import time

session = requests.Session()
response1 = session.get(url="https://httpbin.org/get", params={"employee_id": "EMP001"}, timeout=5)
response1.raise_for_status()
data1 = response1.json()
timeout = 2
max_attempts = 3
base_delay = 1

print("=== NORMAL REQUEST ===")
print(f"Status: {response1.status_code}")
print(f"Employee ID: {data1['args']['employee_id']}")
print("Result: SUCCESS")
print("\n=== SERVICE UNAVAILABLE ===")
for attempt in range(1, max_attempts + 1):
    response2 = session.get(url="https://httpbin.org/status/503", timeout=timeout)
    print(f"Attempt: {attempt}")
    print(f"Status: {response2.status_code}")

    if response2.status_code != 503:
        response2.raise_for_status()
        print("Result: SUCCESS")
        break
    elif attempt < max_attempts:
        delay = base_delay * 2 ** (attempt - 1)
        print(f"Waiting: {delay} seconds")
        print("Result: RETRYING\n")
        time.sleep(delay)
        continue
    else:
        print("Result: FAILED")

try:
    response3 = session.get(url="https://httpbin.org/delay/5", timeout=timeout)
    response3.raise_for_status()
except requests.exceptions.Timeout:
    print("\n=== TIMEOUT ===")
    print("Result: REQUEST TIMED OUT")

print("\n=== RATE LIMIT ===")
status_response = session.get(url="https://httpbin.org/status/429", timeout=5)
print(f"Status: {status_response.status_code}")

if status_response.status_code == 429:
    headers_response = session.get(
        url="https://httpbin.org/response-headers",
        params={"Retry-After": 3},
        timeout=5,
    )
    retry_after = int(headers_response.headers["Retry-After"])
    print(f"Retry-After: {retry_after} seconds")
    print("Result: RATE LIMITED")
    time.sleep(retry_after)
else:
    status_response.raise_for_status()
