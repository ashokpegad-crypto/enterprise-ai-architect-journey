import requests

session = requests.Session()
url = "https://httpbin.org/get"
session.headers.update({
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"})

response = session.get(url, params={"employee_id": "EMP001"})
response.raise_for_status()
data = response.json()

print("=== SESSION API CALL ===")
print(f"Status: {response.status_code}")
print(f"Employee ID: {data['args']['employee_id']}")
print("Result: SUCCESS")

response2 = session.get(url="https://httpbin.org/status/404")
try:
    response2.raise_for_status()
except requests.exceptions.HTTPError:
    print(f"\n=== FAILED API CALL ===")
    print(f"Status: {response2.status_code}")
    print("Result: HTTP ERROR HANDLED")
    