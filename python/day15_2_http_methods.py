import requests

response1 = requests.get("https://httpbin.org/get")
print(f"GET Status: {response1.status_code}")
print(f"GET method: {response1.request.method}")

response2 = requests.post("https://httpbin.org/post", json={"name": "Ashok", "department": "IT"})
print(f"POST Status: {response2.status_code}")
print(f"POST method: {response2.request.method}")

response3 = requests.put("https://httpbin.org/put", json={"name": "Ashok", "department": "IT", "role": "Pega Developer"})
print(f"PUT Status: {response3.status_code}")
print(f"PUT method: {response3.request.method}")

response4 = requests.delete("https://httpbin.org/delete")
print(f"DELETE Status: {response4.status_code}")
print(f"DELETE method: {response4.request.method}")
print(f"DELETE Response: {response4.json()}")
