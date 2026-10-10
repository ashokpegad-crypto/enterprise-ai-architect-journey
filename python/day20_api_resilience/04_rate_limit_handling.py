import time

import requests

status_url = "https://httpbin.org/status/429"
headers_url = "https://httpbin.org/response-headers"
params = {"Retry-After": 3}

status_response = requests.get(status_url, timeout=5)
headers_response = requests.get(headers_url, params=params, timeout=5)

print("=== RATE LIMIT HANDLING ===")
print(f"Status: {status_response.status_code}")

if status_response.status_code == 429:
    retry_after = int(headers_response.headers["Retry-After"])
    print(f"Retry-After: {retry_after} seconds")
    time.sleep(retry_after)
    print("Result: RATE LIMITED")
