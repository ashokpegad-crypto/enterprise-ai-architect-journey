import requests

session = requests.Session()

url = "https://httpbin.org/headers"
session.headers.update({
    "X-Client-Name": "enterprise-employee-service",
    "Accept": "application/json"
})

response1 = session.get(url)
data = response1.json()
print("=== SESSION REQUEST 1 ===")
print(f"Status: {response1.status_code}")
print(f"Client: {data['headers']['X-Client-Name']}")
print(f"Accept: {data['headers']['Accept']}")

response2 = session.get(url, headers={"X-Client-Name": "employee-report-service"})
data2 = response2.json()
print("\n=== SESSION REQUEST 2 ===")
print(f"Status: {response2.status_code}")
print(f"Client: {data2['headers']['X-Client-Name']}")
print(f"Accept: {data2['headers']['Accept']}")