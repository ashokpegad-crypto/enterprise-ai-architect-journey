import requests

max_retries = 3
timeout = 2
url = "https://httpbin.org/status/503"
session = requests.Session()

print("=== RETRY DEMONSTRATION ===")

for attempt in range(1, max_retries + 1):
    response = session.get(url, timeout=timeout)
    print(f"Attempt: {attempt}")
    print(f"Status: {response.status_code}")

    if response.status_code == 503 and attempt < max_retries:
        print("Result: RETRYING\n")
        continue

    print("Result: FAILED")
