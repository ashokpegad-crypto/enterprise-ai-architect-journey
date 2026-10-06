import jwt

jwt_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJFTVAwMDEiLCJyb2xlIjoiUGVnYURldmVsb3BlciIsImV4cCI6MTgwMDAwMDAwMH0.demo-signature"
jwt_token = jwt.encode({"user": "EMP001", "role": "PegaDeveloper", "exp": 1800000000}, jwt_key, algorithm="HS256")

# Decode the JWT token to show its anatomy
decoded_token = jwt.decode(jwt_token, jwt_key, algorithms=["HS256"])

print("=== JWT ANATOMY ===")
header, payload, signature = jwt_token.split('.')
print(f"Segments: {len(jwt_token.split('.'))}")
header_data = jwt.get_unverified_header(jwt_token)
print(f"Algorithm: {header_data.get('alg', 'N/A')}")
print(f"Type: {header_data.get('typ', 'N/A')}")
print(f"Subject: {decoded_token.get('sub', decoded_token.get('user', 'N/A'))}")
print(f"Role: {decoded_token.get('role', 'N/A')}")
print(f"Expiration: {decoded_token.get('exp', 'N/A')}")
print(f"Signature Present: {bool(signature)}")