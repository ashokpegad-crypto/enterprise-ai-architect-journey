import requests

headers = {
    "Authorization": "Bearer DAY17-DEMO-TOKEN",
    "X-Client-Name": "enterprise-employee-service" }

response = requests.get("https://httpbin.org/headers", headers=headers)
data = response.json()
print("=== BEARER TOKEN REQUEST ===")
print(f"Status: {response.status_code}")
print(f"Authorization: {data['headers']['Authorization']}")
print(f"Client: {data['headers']['X-Client-Name']}")