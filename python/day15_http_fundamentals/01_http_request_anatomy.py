import requests

params = {
    "employee_id": "EMP001",
    "department": "IT" }

headers = {
    "X-Employee-Client": "Day15"}

response = requests.get("https://httpbin.org/get", params=params, headers=headers)

data = response.json()

print(f"Status Code: {response.status_code}")
print(f"Request URL: {data['url']}")
print(f"Query params: {data['args']}")
print(f"Custom Header: {data['headers']['X-Employee-Client']}")