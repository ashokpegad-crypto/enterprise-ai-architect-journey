# Day 19 - External API Integration

## Status

**COMPLETED**

Day 19 moved from Python HTTP client mechanics into working external API integration using a real public external service.

### Roadmap target

- External API integration
- Working integration

Day 18 covered Python HTTP clients. Day 20 moves to resilience: timeouts, retries, exponential backoff, and rate limits.

---

## 1. Learning Focus

The day emphasized practical integration-layer thinking rather than repeating basic REST theory.

Key areas:

- Calling a real external API
- Understanding external response shapes
- Processing object and collection responses
- Combining results from multiple endpoints
- Calculating application-level values from external data
- Normalizing an external schema into application-oriented data
- Making the integration reusable through runtime input
- Handling an external 404 without a traceback

---

## 2. Core Mental Model

~~~text
External API
    |
    v
External response schema
    |
    v
Integration / normalization layer
    |
    +--> extract
    +--> combine
    +--> calculate
    +--> normalize
    |
    v
Application-level data
~~~

The key principle is:

> The external API owns its contract; the consuming application decides which fields it needs and how those fields are represented internally.

---

## 3. External API Used

The exercises used GitHub public user and repository endpoints:

~~~text
GET https://api.github.com/users/octocat
GET https://api.github.com/users/octocat/repos
~~~

The Session used:

~~~text
Accept: application/vnd.github+json
X-Client-Name: enterprise-ai-architect-journey
~~~

No authentication token was required for the selected public endpoints.

---

## 4. Exercise 1 - GitHub User Integration

### File

`python/day19_external_api_integration/01_github_user_integration.py`

### Objective

Call a real GitHub user endpoint and extract selected fields from the JSON response.

### Implementation

~~~python
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
~~~

### Actual output captured

~~~text
=== GITHUB USER INTEGRATION ===
Status: 200
Username: octocat
External ID: 583231
Name: The Octocat
Public Repositories: 8
Followers: 24475
~~~

### Review

**10/10**

Demonstrated correctly:

- Reusable Session
- External API call
- HTTP status validation
- JSON parsing
- Selective field extraction

---

## 5. Exercise 2 - GitHub Repository Collection Integration

### File

`python/day19_external_api_integration/02_github_repository_integration.py`

### Objective

Process a collection response where the top-level JSON value is a Python list and each repository is represented by a dictionary.

### Core implementation

~~~python
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
    print("---")
~~~

### Actual output captured

~~~text
=== GITHUB REPOSITORIES ===
Status: 200
Repositories count: 8
boysenberry-repo-1 | None | 482
git-consortium | None | 617
hello-worId | None | 818
Hello-World | None | 3851
linguist | Ruby | 768
octocat.github.io | CSS | 1179
Spoon-Knife | HTML | 14082
test-repo1 | None | 492
~~~

### Review

**10/10**

The response was correctly understood as:

~~~text
data
 |
 +-- repository dictionary
 +-- repository dictionary
 +-- repository dictionary
 ...
~~~

The exercise also demonstrated that `None` is valid response data when the external service has no language value for a repository.

---

## 6. Exercise 3 - Multi-Endpoint GitHub User Summary

### File

`python/day19_external_api_integration/03_github_user_summary.py`

### Objective

Call two external endpoints and combine their information into one application-level result.

### Key implementation

~~~python
response1 = session.get("https://api.github.com/users/octocat")
response1.raise_for_status()
data1 = response1.json()

response2 = session.get(
    url="https://api.github.com/users/octocat/repos"
)
response2.raise_for_status()
data2 = response2.json()

print("=== GITHUB USER SUMMARY ===")
print(f"User: {data1['login']}")
print(f"Name: {data1['name']}")
print(f"Public Repositories: {data1['public_repos']}")
print(f"Repositories Returned: {len(data2)}")
print(f"Followers: {data1['followers']}")
print(f"Total Stars: {sum(repo['stargazers_count'] for repo in data2)}")
~~~

### Actual output captured

~~~text
=== GITHUB USER SUMMARY ===
User: octocat
Name: The Octocat
Public Repositories: 8
Repositories Returned: 8
Followers: 24475
Total Stars: 22291
~~~

### Review

**10/10**

Important distinction reinforced:

- `public_repos` came from the user endpoint.
- `len(data2)` came from the repository endpoint.
- `total_stars` was calculated from the repository collection.

This distinction becomes important when external collection endpoints introduce pagination.

---

## 7. Exercise 4 - GitHub Data Normalization

### File

`python/day19_external_api_integration/04_github_data_normalization.py`

### Objective

Translate GitHub's external field names into application-oriented names.

### Normalized repository representation

~~~python
repositories = [
    {
        "repository_name": repo["name"],
        "url": repo["html_url"],
        "language": repo["language"],
        "stars": repo["stargazers_count"],
    }
    for repo in data2
]
~~~

### Normalized user representation

~~~python
github_summary = {
    "username": data1["login"],
    "display_name": data1["name"],
    "repository_count": data1["public_repos"],
    "followers": data1["followers"],
    "total_stars": sum(repo["stars"] for repo in repositories),
}
~~~

### Mapping

~~~text
GitHub field          Application field
---------------------------------------
login             ->  username
name              ->  display_name
public_repos      ->  repository_count
followers         ->  followers
name              ->  repository_name
html_url          ->  url
language          ->  language
stargazers_count  ->  stars
~~~

### Actual output captured

~~~text
=== NORMALIZED GITHUB USER ===
Username: octocat
Display Name: The Octocat
Repository Count: 8
Followers: 24479
Total Stars: 22293

=== NORMALIZED REPOSITORIES ===
8 repository records normalized successfully.
Language values returned as None were preserved.
~~~

### Review

**10/10**

This exercise established the integration-layer boundary between the external API schema and the application's internal representation.

---

## 8. Exercise 5 - Reusable GitHub User Lookup

### File

`python/day19_external_api_integration/05_github_user_lookup.py`

### Objective

Make the external API operation reusable by accepting the GitHub username at runtime and handling the demonstrated 404 path without a traceback.

### Key implementation

~~~python
username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}"

response = session.get(url)

try:
    response.raise_for_status()
    data = response.json()

    # extract and print application fields

except requests.exceptions.HTTPError:
    print(f"Status: {response.status_code}")
    print("Result: USER NOT FOUND")
~~~

### Success output captured

~~~text
Enter GitHub username: octocat
=== GITHUB USER LOOKUP ===
Status: 200
Username: octocat
External ID: 583231
Name: The Octocat
Public Repositories: 8
Followers: 24480
Result: SUCCESS
~~~

### 404 output captured

~~~text
Enter GitHub username: [empty input]
=== GITHUB USER LOOKUP ===
Status: 404
Result: USER NOT FOUND
~~~

### Review

**Accepted as completed.**

The demonstrated integration correctly handled the successful 200 response and the 404 response.

### Production-quality refinement recorded

The current exception handler labels every `HTTPError` as `USER NOT FOUND`.

A production implementation should distinguish the HTTP status:

~~~text
404 -> USER NOT FOUND
other 4xx/5xx -> appropriate HTTP/API error handling
~~~

This was recorded as an engineering improvement without extending the day unnecessarily.

---

## 9. Day 19 Key Integration Patterns

| Pattern | Demonstrated behavior |
|---|---|
| Real external API | GitHub public user and repository endpoints |
| Object response | Dictionary field extraction |
| Collection response | List of repository dictionaries |
| Multi-endpoint composition | User endpoint + repository endpoint |
| Derived data | Total star calculation |
| Schema normalization | External GitHub names mapped to application names |
| Reusable lookup | Runtime username converted to endpoint path |
| External error handling | 404 path handled without traceback |

---

## 10. Integration Architecture

~~~text
+----------------------+       +-------------------------+
| Python requests     | ----> | GitHub User API         |
| Session             |       +-----------+-------------+
+----------------------+                   |
                                           | user JSON
                                           v
                                +----------+-----------+
                                | Integration Layer    |
                                | - extract            |
                                | - combine            |
                                | - calculate          |
                                | - normalize          |
                                +----------+-----------+
                                           |
                                           v
                                  Application data
                                           ^
                                           |
                                +----------+-----------+
                                | GitHub Repository API|
                                +----------------------+
~~~

The architectural separation is the important lesson:

~~~text
External schema
      |
      v
Integration layer
      |
      v
Application schema
~~~

This reduces direct coupling between application code and external API field names.

---

## 11. Day 19 Validation

| Area | Result |
|---|---|
| Real external API call | Pass |
| Collection processing | Pass |
| Multi-endpoint integration | Pass |
| Derived application data | Pass |
| Data normalization | Pass |
| Runtime user lookup | Pass |
| Controlled 404 handling | Pass |
| HTTP response validation | Pass |

### Final status

**DAY 19 - COMPLETED**

The day successfully produced a working external API integration foundation.

---

## 12. Scope Intentionally Deferred

The following were deliberately not introduced:

- Pagination
- Timeouts
- Retries
- Exponential backoff
- Rate-limit handling
- Database persistence
- FastAPI
- Async HTTP
- httpx
- Authentication tokens for these public endpoints

These belong to later roadmap stages.

---

## 13. Day 19 Final Mental Model

~~~text
External API contract
        |
        v
requests.Session()
        |
        v
GET external endpoint
        |
        v
raise_for_status()
        |
        v
response.json()
        |
        +--> object response -> extract
        |
        +--> collection response -> iterate / calculate
        |
        +--> multiple endpoints -> combine
        |
        +--> external fields -> normalize
        |
        v
Application-level data
~~~

---

## 14. Next Roadmap Step

~~~text
Day 19
External API Integration
        |
        v
Day 20
Timeouts + Retries + Exponential Backoff + Rate Limits
        |
        v
Day 21
Review
~~~

Day 19 establishes the working integration foundation. Day 20 will focus on resilience when external systems are slow, unavailable, overloaded, or rate-limiting clients.
