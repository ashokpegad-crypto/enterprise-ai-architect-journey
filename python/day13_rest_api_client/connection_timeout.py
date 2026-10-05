import requests

try:
    response = requests.get(url="http://localhost:9999", timeout=3)
    print(f"Status code {response.status_code}")

    response.raise_for_status()

    print("Request succeeded")
except requests.exceptions.Timeout as error:
    print(f"Request timed out: {error}")
except requests.exceptions.ConnectionError as error:
    print(f"Connection failed: {error}")