import requests

session = requests.Session()
url = "https://httpbin.org/headers"
session.headers.update({
    "Authorization": "Bearer DAY17-DEMO-TOKEN",
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"
})

response1 = session.get(url)
data1 = response1.json()
print("=== EMPLOYEE API REQUEST ===")
print(f"Status: {response1.status_code}")
print(f"client: {data1['headers']['X-Client-Name']}")
print(f"Accept: {data1['headers']['Accept']}")

response2 = session.get(url="https://httpbin.org/get", params={"employee_id": "EMP001", "department": "IT"})
data2 = response2.json()
print("\n=== EMPLOYEE SEARCH REQUEST ===")
print(f"Status: {response2.status_code}")
print(f"Authentication Present: {bool(data2['headers']['Authorization'])}")
print(f"Client: {data2['headers']['X-Client-Name']}")
print(f"Employee ID: {data2['args']['employee_id']}")
print(f"Department: {data2['args']['department']}")