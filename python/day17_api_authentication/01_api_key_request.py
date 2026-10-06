import requests

headers = {
    "X-API-Key": "DAY17-DEMO-KEY",
    "X-Client-Name": "enterprise-employee-service" }

response = requests.get("https://httpbin.org/headers", headers=headers)
data = response.json()
print("=== API KEY REQUEST ===")
print(f"Status: {response.status_code}")
print(f"API Key: {data['headers']['X-Api-Key']}")
print(f"Client: {data['headers']['X-Client-Name']}")