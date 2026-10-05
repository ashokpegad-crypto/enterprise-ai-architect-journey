import requests

try:
    response = requests.get(url="https://httpbin.org/delay/5", timeout=2)
    print(f"Status Code: {response.status_code}")

    response.raise_for_status()

    print("Request suceeded")
except requests.exceptions.Timeout as error:
    print(f"Request time out: {error}")