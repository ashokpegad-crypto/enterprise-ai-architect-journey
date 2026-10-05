import requests

employee = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "active": True
}

response = requests.post(url="https://httpbin.org/post", json=employee)
print(f"Status code: {response.status_code}")

data = response.json()

print(f"Request: {data['data']}")
print(f"Response: {data['json']}")