import requests

json_data = {
    "name": "Ashok",
    "department": "IT",
    "role": "Pega Developer"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post("https://httpbin.org/post", json=json_data, headers=headers)
print(f"Status Code: {response.status_code}")

data = response.json()
print(f"Content-Type Header: {data['headers']['Content-Type']}")
print(f"Accept Header: {data['headers']['Accept']}")
print(f"Employee Name: {data['json']['name']}")
print(f"Department: {data['json']['department']}")
print(f"Role: {data['json']['role']}")