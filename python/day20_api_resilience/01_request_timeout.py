import requests

session = requests.Session()
session.headers.update({
    "Accept": "application/json",
    "X-Client-Name": "enterprise-ai-architect-journey"
})

response1 = session.get(
    url="https://httpbin.org/get",
    timeout=5,
    params={"employee_id": "EMP001"}
)
response1.raise_for_status()
data1 = response1.json()

print("=== FAST API CALL ===")
print(f"Status: {response1.status_code}")
print(f"Employee ID: {data1['args']['employee_id']}")
print("Result: SUCCESS")

try:
    response2 = session.get(
        url="https://httpbin.org/delay/5",
        timeout=2
    )
    response2.raise_for_status()
except requests.exceptions.Timeout:
    print("\n=== TIMEOUT API CALL ===")
    print("Result: REQUEST TIMED OUT")
