import requests

session = requests.Session()
url = "https://httpbin.org/get"
session.headers.update({
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"})

response = session.get(url, params={"employee_id": "EMP001"})
response.raise_for_status()
data = response.json()

json_data = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "role": "Pega Developer"
}

response2 = session.post(url="https://httpbin.org/post", json=json_data)
response2.raise_for_status()
employee_data = response2.json()

print("=== GET EMPLOYEE ===")
print(f"Status: {response.status_code}")
print(f"Employee ID: {data['args']['employee_id']}")
print("\n=== CREATE EMPLOYEE ===")
print(f"Status: {response2.status_code}")
print(f"Employee ID: {employee_data['json']['employee_id']}")
print(f"Name: {employee_data['json']['name']}")
print(f"Department: {employee_data['json']['department']}")
print(f"Role: {employee_data['json']['role']}")
print("Result: SUCCESS")