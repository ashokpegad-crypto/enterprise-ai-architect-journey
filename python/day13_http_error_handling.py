import requests

url = "https://httpbin.org/status/200"

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    response.raise_for_status()

    print("Request Succeded")

except requests.exceptions.HTTPError as error:
    print(f"API request failed: {error}")