import requests

status_codes = [200, 201, 204, 400, 401, 403, 404, 500]

for code in status_codes:
    response = requests.get(f"https://httpbin.org/status/{code}")
    print(f"Status Requested: {code}")
    print(f"Status Received: {response.status_code}")
    print()