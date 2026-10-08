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

repositories = [
    {
        "repository_name": repo["name"],
        "url": repo["html_url"],
        "language": repo["language"],
        "stars": repo["stargazers_count"],
    }
    for repo in data2
]

github_summary = {
    "username": data1["login"],
    "display_name": data1["name"],
    "repository_count": data1["public_repos"],
    "followers": data1["followers"],
    "total_stars": sum(repo["stars"] for repo in repositories),
}

print("=== NORMALIZED GITHUB USER ===")
print(f"Username: {github_summary['username']}")
print(f"Display Name: {github_summary['display_name']}")
print(f"Repository Count: {github_summary['repository_count']}")
print(f"Followers: {github_summary['followers']}")
print(f"Total Stars: {github_summary['total_stars']}")
print("\n=== NORMALIZED REPOSITORIES ===")
for repo_count, repo in enumerate(repositories, start=1):
    print(f"Repository {repo_count}")
    print(f"Name: {repo['repository_name']}")
    print(f"HTML URL: {repo['url']}")
    print(f"Language: {repo['language']}")
    print(f"Stars: {repo['stars']}")
    print("---")
