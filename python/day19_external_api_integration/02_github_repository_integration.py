import requests

session = requests.Session()
session.headers.update({
    "Accept": "application/vnd.github+json",
    "X-Client-Name": "enterprise-ai-architect-journey"
})
url = "https://api.github.com/users/octocat/repos"

response = session.get(url)
response.raise_for_status()
data = response.json()
print("=== GITHUB REPOSITORIES ===")
print(f"Status: {response.status_code}")
print(f"Repositories count: {len(data)}")
for repo in data:
    print(f"Name: {repo['name']}")
    print(f"HTML URL: {repo['html_url']}")
    print(f"Language: {repo['language']}")
    print(f"Stars: {repo['stargazers_count']}")
<<<<<<< HEAD
    print("---")
=======
    print("---")
>>>>>>> 59c915183690cb4f809e962c46043f11ebac5c29
