import time

import requests

url = "https://httpbin.org/status/503"
max_attempts = 3
timeout = 2
base_delay = 1

session = requests.Session()

print("=== EXPONENTIAL BACKOFF ===")

for attempt in range(1, max_attempts + 1):
    response = session.get(url, timeout=timeout)
    print(f"Attempt: {attempt}")
    print(f"Status: {response.status_code}")

    if response.status_code == 503 and attempt < max_attempts:
        delay = base_delay * 2 ** (attempt - 1)
        print(f"Waiting: {delay} seconds")
        print("Result: RETRYING\n")
        time.sleep(delay)
        continue

    print("Result: FAILED")
