import requests

params = {
    "userId": "1"
}

response1 = requests.get(url = "https://jsonplaceholder.typicode.com/todos/1")
data1 = response1.json()
print("Path Status Code:", response1.status_code)
print("Todo ID:", data1['id'])
print("Todo Title:", data1['title'])

response2 = requests.get(url = "https://jsonplaceholder.typicode.com/todos", params=params)
data2 = response2.json()
print("Query Status Code:", response2.status_code)
print("First Todo ID:", data2[0]['id'])
print("Todos for User 1:", len(data2))