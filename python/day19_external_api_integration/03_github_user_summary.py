import requests

session = requests.Session()
session.headers.update({
    "Accept": "application/vnd.github+json",
    "X-Client-Name": "enterprise-ai-architect-journey"
})
url = "https://api.github.com/users/octocat"

response1 = session.get(url)
response1.raise_for_status()
data1 = response1.json()

response2 = session.get(url=f"{url}/repos")
response2.raise_for_status()
data2 = response2.json()


print("=== GITHUB USER SUMMARY ===")
print(f"User: {data1['login']}")
print(f"Name: {data1['name']}")
print(f"Public Repositories: {data1['public_repos']}")
print(f"Repositories Returned: {len(data2)}")
print(f"Followers: {data1['followers']}")
print(f"Total Stars: {sum(repo['stargazers_count'] for repo in data2)}")

