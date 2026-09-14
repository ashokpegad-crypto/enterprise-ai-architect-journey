import json

customer = {
    "customer_id": "CUST001",
    "customer_name": "Ashok",
    "customer_type": "Gold",
    "active": True,
    "total_cases": 5
}

with open("customer.json", "w") as file:
    json.dump(customer, file, indent=4)

    print("Customer data has been written to customer.json")