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
