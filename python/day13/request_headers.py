import requests

headers = {
    "X-Employee-Client": "Day13"
    }

response = requests.get(url="https://httpbin.org/headers", headers=headers)
print(f"Status code: {response.status_code}")

data = response.json()

print(data["headers"])