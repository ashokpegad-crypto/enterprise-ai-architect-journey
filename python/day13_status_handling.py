import requests


url = "https://httpbin.org/status/404"

response = requests.get(url)

print(f"Status Code: {response.status_code}")

response.raise_for_status()