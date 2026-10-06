# Day 17 - API Authentication

## Status

**COMPLETED**

Day 17 covered the authentication stage of Week 3 — APIs.

### Roadmap target

- API keys
- OAuth basics
- JWT
- Authenticated request

Day 18 moves to Python HTTP clients, Day 19 to external API integration, and Day 20 to timeout/retry/exponential-backoff/rate-limit resilience.

---

## 1. Day 17 Learning Approach

Because the learner already has 5–6 years of REST integration experience in Pega, Day 17 minimized basic authentication theory and emphasized:

- exact HTTP request construction
- where credentials/tokens are sent
- PyJWT creation and verification mechanics
- JWT claim mapping
- authentication failure behavior
- OAuth Client Credentials request shape
- access-token to Bearer-token flow

The learning method was corrected during the day to avoid hidden prerequisites: every new Python/library concept was explained before it became an exercise requirement.

---

## 2. Authentication Mental Model

~~~text
API Key
  -> client credential
  -> X-API-Key: <key>

Bearer Token
  -> access credential
  -> Authorization: Bearer <token>

JWT
  -> structured signed token
  -> HEADER.PAYLOAD.SIGNATURE

OAuth Client Credentials
  -> client_id + client_secret
  -> token endpoint
  -> access_token
  -> Authorization: Bearer <access_token>
  -> protected API
~~~

Important distinctions:

- API key is a credential pattern.
- OAuth is an authorization/token acquisition framework.
- JWT is a structured token format.
- A bearer access token may be an opaque token or may contain a JWT.

---

## 3. Exercise 1 — API Key Request

### File

`python/day17_api_authentication/01_api_key_request.py`

### Objective

Send a demo API key in a request header and inspect the echoed response.

### Implementation

~~~python
import requests

headers = {
    "X-API-Key": "DAY17-DEMO-KEY",
    "X-Client-Name": "enterprise-employee-service" }

response = requests.get("https://httpbin.org/headers", headers=headers)
data = response.json()
print("=== API KEY REQUEST ===")
print(f"Status: {response.status_code}")
print(f"API Key: {data['headers']['X-Api-Key']}")
print(f"Client: {data['headers']['X-Client-Name']}")
~~~

### Actual output

~~~text
=== API KEY REQUEST ===
Status: 200
API Key: DAY17-DEMO-KEY
Client: enterprise-employee-service
~~~

### Review

**10/10**

The request header was constructed correctly and the returned values were extracted from the response.

Important: httpbin was used as an inspection/echo endpoint. A 200 response did not validate the demo API key.

---

## 4. Exercise 2 — Bearer Token Request

### File

`python/day17_api_authentication/02_bearer_token_request.py`

### Objective

Send a bearer token in the standard Authorization header.

### Implementation

~~~python
import requests

headers = {
    "Authorization": "Bearer DAY17-DEMO-TOKEN",
    "X-Client-Name": "enterprise-employee-service" }

response = requests.get("https://httpbin.org/headers", headers=headers)
data = response.json()
print("=== BEARER TOKEN REQUEST ===")
print(f"Status: {response.status_code}")
print(f"Authorization: {data['headers']['Authorization']}")
print(f"Client: {data['headers']['X-Client-Name']}")
~~~

### Actual output

~~~text
=== BEARER TOKEN REQUEST ===
Status: 200
Authorization: Bearer DAY17-DEMO-TOKEN
Client: enterprise-employee-service
~~~

### Review

**10/10**

The Authorization header and Bearer scheme were implemented correctly.

---

## 5. Exercise 3 — JWT Creation, Verification & Claim Mapping

### File

`python/day17_api_authentication/03_jwt_creation_verification.py`

### Core mechanics

JWT:

~~~text
HEADER.PAYLOAD.SIGNATURE
~~~

PyJWT operations learned:

~~~text
jwt.encode(...)
    -> create/sign token

jwt.get_unverified_header(...)
    -> inspect header metadata

jwt.decode(...)
    -> verify signature and return validated claims
~~~

### Implementation

~~~python
import jwt

payload = {
  "sub": "EMP001",
  "role": "PegaDeveloper",
  "department": "IT",
  "exp": 1800000000
}
key = "day17-demo-secret-0123456789abcdef"
jwt_token = jwt.encode(payload, key, algorithm="HS256")

segments = jwt_token.split(".")
header, encoded_payload, signature = segments
header_data = jwt.get_unverified_header(jwt_token)
verified_payload = jwt.decode(jwt_token, key, algorithms=["HS256"])

employee_id = verified_payload["sub"]
role = verified_payload["role"]
department = verified_payload["department"]
expiration = verified_payload["exp"]

print("=== JWT CREATION & VERIFICATION ===")
print(f"Token Created: {bool(jwt_token)}")
print(f"Segments: {len(segments)}")
print(f"Algorithm: {header_data.get('alg', 'N/A')}")
print(f"Type: {header_data.get('typ', 'N/A')}")
print(f"Signature Present: {bool(signature)}")
print(f"Verified: {bool(verified_payload)}")
print(f"Employee ID: {employee_id}")
print(f"Role: {role}")
print(f"Department: {department}")
print(f"Expiration: {expiration}")

correct_key_result = "PASS"
try:
    jwt.decode(
        jwt_token,
        "wrong-demo-secret-0123456789abcdef",
        algorithms=["HS256"],
    )
    wrong_key_result = "PASS"
except jwt.InvalidSignatureError:
    wrong_key_result = "FAIL"

print()
print("=== JWT VERIFICATION FAILURE ===")
print(f"Correct Key: {correct_key_result}")
print(f"Wrong Key: {wrong_key_result}")
~~~

### Actual output

~~~text
=== JWT CREATION & VERIFICATION ===
Token Created: True
Segments: 3
Algorithm: HS256
Type: JWT
Signature Present: True
Verified: True
Employee ID: EMP001
Role: PegaDeveloper
Department: IT
Expiration: 1800000000

=== JWT VERIFICATION FAILURE ===
Correct Key: PASS
Wrong Key: FAIL
~~~

### Review

**10/10 after correction**

The first implementation used a 17-byte demo HS256 key and produced an InsecureKeyLengthWarning. The implementation was corrected to use a 32+ byte demo secret.

### Claim mapping

~~~text
JWT claim       Application value
---------------------------------
sub             employee_id
role            role
department      department
exp             expiration
~~~

Important: JWT claim mapping is application-defined. The JWT does not automatically know that `sub` should become `employee_id`.

### Verification mental model

~~~text
JWT
  -> trusted key
  -> trusted allowed algorithm
  -> signature verification
  -> applicable claim validation
  -> verified claims
  -> application mapping
~~~

Manual header inspection is useful for learning/debugging, but unverified token data must not be treated as trusted authentication data.

---

## 6. Exercise 4 — JWT Verification Failure

The Day 17 JWT verification failure scenario was consolidated into Exercise 3 rather than maintained as a separate coding file.

### Scenario tested

The same JWT was decoded using:

- the correct HS256 key
- a different HS256 key

### Expected behavior

~~~text
Correct key
  -> verification succeeds

Wrong key
  -> signature mismatch
  -> jwt.InvalidSignatureError
  -> verification fails
~~~

This made the security boundary concrete without adding a duplicate JWT exercise.

---

## 7. Exercise 5 — OAuth Client Credentials Flow

### File

`python/day17_api_authentication/05_oauth_client_credentials_request.py`

### Objective

Construct an OAuth Client Credentials token request, inspect its request shape, then use a simulated access token as a Bearer credential for a protected-API-style request.

### Implementation

~~~python
import requests

token_url = "https://httpbin.org/post"
client_id = "enterprise-employee-service"
client_secret = "DAY17-DEMO-SECRET"

data = {
    "grant_type": "client_credentials",
    "scope": "employees.read" }
response = requests.post(token_url, data=data, auth=(client_id, client_secret))
response.raise_for_status()
response_data = response.json()

token_response_data = {
    "access_token": "DAY17-DEMO-ACCESS-TOKEN",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "employees.read"
}

access_token = token_response_data["access_token"]
token_type = token_response_data["token_type"]
scope = token_response_data["scope"]

api_header = {"Authorization": f"{token_type} {access_token}"}

api_response = requests.get("https://httpbin.org/get", headers=api_header)
api_response.raise_for_status()

print("=== OAUTH CLIENT CREDENTIALS FLOW ===")
print(f"Token Request Status: {response.status_code}")
print(f"Grant Type: {data['grant_type']}")
print(f"Scope: {data['scope']}")
print(f"Client ID sent: {client_id}")
print("\n=== ACCESS TOKEN ===")
print(f"Token Type: {token_type}")
print(f"Access Token: {access_token}")
print(f"Expires In: {token_response_data['expires_in']}")
print(f"Scope: {scope}")
print("\n=== PROTECTED API REQUEST ===")
print(f"API Request Status: {api_response.status_code}")
print(f"Authorization Header Sent: {api_header['Authorization']}")
~~~

### Actual output

~~~text
=== OAUTH CLIENT CREDENTIALS FLOW ===
Token Request Status: 200
Grant Type: client_credentials
Scope: employees.read
Client ID sent: enterprise-employee-service

=== ACCESS TOKEN ===
Token Type: Bearer
Access Token: DAY17-DEMO-ACCESS-TOKEN
Expires In: 3600
Scope: employees.read

=== PROTECTED API REQUEST ===
API Request Status: 200
Authorization Header Sent: Bearer DAY17-DEMO-ACCESS-TOKEN
~~~

### OAuth request mechanics

~~~text
POST <token-endpoint>

Authentication:
client_id + client_secret
        -> HTTP Basic client authentication

Form body:
grant_type=client_credentials
scope=employees.read

Token response:
access_token
token_type
expires_in
scope

Protected API:
Authorization: Bearer <access_token>
~~~

### Important code details

`data=data` was used for the OAuth token request rather than `json=data` because the exercise modeled a form-encoded token request.

`auth=(client_id, client_secret)` lets the Python requests library construct HTTP Basic client authentication for the token request.

The protected API request used only the access token, not the client secret.

### Environment limitation

The open endpoint used for the exercise did not act as a real OAuth authorization server. Therefore:

- the token request was a real HTTP request whose shape was inspected
- the access-token response was simulated
- the protected API request was a real HTTP request whose Bearer header was inspected
- a real authorization server issuing a token was not implemented
- a real protected API validating that OAuth token was not implemented

This is intentionally recorded as a scope limitation rather than treating httpbin as a production identity provider.

---

## 8. Real-World OAuth/JWT Follow-Up

A true end-to-end scenario should later use a controlled authorization server/identity provider and a protected API so that the following chain is real:

~~~text
Client application
      |
      | client authentication
      v
Authorization Server
      |
      | access token
      v
Client
      |
      | Authorization: Bearer <access_token>
      v
Protected API
      |
      | token verification/validation
      v
Application authorization
~~~

This will be revisited at a later integration/project stage rather than using a fake local implementation and calling it real-time.

---

## 9. Day 17 Final Knowledge Model

~~~text
API Key
  -> credential sent with API request

Bearer Token
  -> credential sent in Authorization header

JWT
  -> structured signed token
  -> HEADER.PAYLOAD.SIGNATURE

OAuth
  -> token acquisition/authorization framework

Client Credentials
  -> client_id + client_secret
  -> token endpoint
  -> access_token
  -> Bearer access to API

JWT verification
  -> trusted key
  -> explicit allowed algorithm
  -> signature verification
  -> claim validation
  -> claim mapping
~~~

---

## 10. Day 17 Definition of Done

- API key placement understood and implemented
- Bearer token placement understood and implemented
- JWT anatomy understood
- JWT creation implemented with PyJWT
- JWT signature verification implemented
- Wrong-key verification failure demonstrated
- JWT claims mapped into application values
- HS256 key-length warning understood and corrected
- OAuth Client Credentials request constructed
- Form data vs JSON request body distinction understood for token requests
- HTTP Basic client authentication understood in code
- Access token mapped into Bearer Authorization header
- Difference between an open inspection endpoint and a real authorization server/protected API understood

---

## 11. Explicitly Deferred

- Authorization Code / PKCE
- Refresh-token architecture
- RSA/RS256 implementation
- JWKS and key rotation
- Full identity-provider deployment
- Advanced scope/role architecture
- FastAPI authentication
- Timeout/retry/rate-limit resilience
- Real end-to-end OAuth identity-provider integration

---

## 12. Day 18 Bridge

Day 17 answered:

> How do I authenticate an API request and handle common credential/token forms?

Day 18 moves to:

> How do I design a reusable Python HTTP client that handles these authenticated requests cleanly?

~~~text
Day 15 -> HTTP fundamentals
      ↓
Day 16 -> REST API design
      ↓
Day 17 -> API authentication
      ↓
Day 18 -> Python HTTP clients
      ↓
Day 19 -> External API integration
      ↓
Day 20 -> Resilient client behavior
~~~

---

## Final Status

**DAY 17 — COMPLETED**

Day 17 established the practical authentication foundation required for the next API-engineering stages while keeping real identity-provider integration explicitly deferred to a later integration/project stage.
