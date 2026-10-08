import requests

session = requests.Session()
username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}"
session.headers.update({
    "Accept": "application/vnd.github+json",
    "X-Client-Name": "enterprise-ai-architect-journey"
})

response = session.get(url)
try:
    response.raise_for_status()
    data = response.json()
    print("=== GITHUB USER LOOKUP ===")
    print(f"Status: {response.status_code}")
    print(f"Username: {data['login']}")
    print(f"External ID: {data['id']}")
    print(f"Name: {data['name']}")
    print(f"Public Repositories: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print("Result: SUCCESS")
except requests.exceptions.HTTPError:
    print("=== GITHUB USER LOOKUP ===")
    print(f"Status: {response.status_code}")
    print("Result: USER NOT FOUND")
