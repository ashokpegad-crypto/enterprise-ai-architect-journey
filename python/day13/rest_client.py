import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print(f"Status Code: {response.status_code}")

data = response.json()

print(f"Todo ID: {data['id']}")
print(f"Title: {data['title']}")
print(f"Completed: {data['completed']}")