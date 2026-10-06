import base64
import json

import jwt

payload = {
    "sub": "EMP001",
    "role": "PegaDeveloper",
    "department": "IT",
    "exp": 1800000000,
}
key = "day17-demo-secret-0123456789abcdef"
jwt_token = jwt.encode(payload, key, algorithm="HS256")

jwt.decode(jwt_token, key, algorithms=["HS256"])
print("=== JWT VERIFICATION ===")
print("Valid Token: PASS")

try:
    jwt.decode(
        jwt_token,
        "wrong-demo-secret-0123456789abcdef",
        algorithms=["HS256"],
    )
except jwt.InvalidSignatureError as error:
    print("Wrong Key: FAIL")
    print(f"Wrong Key Exception: {type(error).__name__}")
else:
    print("Wrong Key: PASS")

header, encoded_payload, signature = jwt_token.split(".")
payload_bytes = base64.urlsafe_b64decode(
    encoded_payload + "=" * (-len(encoded_payload) % 4)
)
tampered_payload = json.loads(payload_bytes)
tampered_payload["role"] = "Admin"
tampered_payload_segment = (
    base64.urlsafe_b64encode(
        json.dumps(tampered_payload, separators=(",", ":")).encode("utf-8")
    )
    .decode("ascii")
    .rstrip("=")
)
tampered_token = f"{header}.{tampered_payload_segment}.{signature}"

try:
    jwt.decode(tampered_token, key, algorithms=["HS256"])
except jwt.InvalidSignatureError as error:
    print("Tampered Token: FAIL")
    print(f"Tampered Token Exception: {type(error).__name__}")
else:
    print("Tampered Token: PASS")

expired_payload = {**payload, "exp": 1}
expired_token = jwt.encode(expired_payload, key, algorithm="HS256")

try:
    jwt.decode(expired_token, key, algorithms=["HS256"])
except jwt.ExpiredSignatureError as error:
    print("Expired Token: FAIL")
    print(f"Expired Token Exception: {type(error).__name__}")
else:
    print("Expired Token: PASS")
