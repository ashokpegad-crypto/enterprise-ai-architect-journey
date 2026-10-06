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
