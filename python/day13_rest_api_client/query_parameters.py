import requests

params = {
    "employee_id": "EMP001",
    "department": "IT"
}

response = requests.get(url="https://httpbin.org/get", params=params)
print(f"Status code: {response.status_code}")

data = response.json()

print(data["args"])