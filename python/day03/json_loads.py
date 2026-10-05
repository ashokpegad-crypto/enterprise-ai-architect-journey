import json

json_text = '{"customer_id": "CUST001", "customer_name": "Ashok", "customer_type": "Gold", "active": true, "total_cases": 5}'
customer = json.loads(json_text)

print("Customer ID:", customer["customer_id"])
print("Customer Name:", customer["customer_name"])
print("Customer Type:", customer["customer_type"])
print("Active:", customer["active"])
print("Total Cases:", customer["total_cases"])
print("Data Type of customer variable:", type(customer))