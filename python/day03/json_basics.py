import json

customer = {
    "customer_id": "CUST001",
    "customer_name": "Ashok",
    "customer_type": "Gold",
    "active": True,
    "total_cases": 5
}

json_text = json.dumps(customer, indent=4)

print("Python Dictionary")
print(customer)
print("\nJSON text")
print(json_text)