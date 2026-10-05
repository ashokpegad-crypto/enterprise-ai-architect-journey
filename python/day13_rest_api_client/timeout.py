import requests

try:
    response = requests.get(url="https://httpbin.org/delay/3", timeout=1)
    print(f"Status code: {response.status_code}")

    response.raise_for_status()

    print("Request suceeded")
except requests.exceptions.Timeout as error:
    print(f"API failed: {error}")