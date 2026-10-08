import requests

session = requests.Session()
url = "https://api.github.com/users/octocat"
session.headers.update({
    "Accept": "application/vnd.github+json",
    "X-Client-Name": "enterprise-ai-architect-journey"
})

response = session.get(url)
response.raise_for_status()
data = response.json()
print("=== GITHUB USER INTEGRATION ===")
print(f"Status: {response.status_code}")
print(f"Username: {data['login']}")
print(f"External ID: {data['id']}")
print(f"Name: {data['name']}")
print(f"Public Repositories: {data['public_repos']}")
print(f"Followers: {data['followers']}")
