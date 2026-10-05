import requests

params = {
    "employee_id": "EMP001",
    "department": "IT" }
headers = {
    "X-Employee-Client": "Day15"}

response = requests.get("https://httpbin.org/get", params=params, headers=headers)
data1 = response.json()
print("==Get Employee==")
print("Status Code:", response.status_code)
print("Employee ID:", data1['args']['employee_id'])
print("Department:", data1['args']['department'])
print("Client:", data1['headers']['X-Employee-Client'])

json_data = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "role": "Pega Developer"}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"}

response2 = requests.post("https://httpbin.org/post", json=json_data, headers=headers)
data2 = response2.json()
print("\n==Post Employee==")
print("Status Code:", response2.status_code)
print("Employee ID:", data2['json']['employee_id'])
print("Name:", data2['json']['name'])
print("Department:", data2['json']['department'])
print("Role:", data2['json']['role'])

json_data = {
    "employee_id": "EMP001",
    "name": "Ashok",
    "department": "IT",
    "role": "Senior Pega Developer"}

response3 = requests.put("https://httpbin.org/put", json=json_data, headers=headers)
data3 = response3.json()
print("\n==Put Employee==")
print("Status Code:", response3.status_code)
print("Employee ID:", data3['json']['employee_id'])
print("Role:", data3['json']['role'])

response4 = requests.delete("https://httpbin.org/delete")
print("\n==Delete Employee==")
print("Status Code:", response4.status_code)
print("Method:", response4.request.method)