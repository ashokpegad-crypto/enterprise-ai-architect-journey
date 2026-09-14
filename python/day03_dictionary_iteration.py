customer = {
    "id": "CUST001",
    "name": "Ashok",
    "type": "Gold",
    "active": True,
    "city": "Bangalore"
}

print("Customer attributes:")

for key, value in customer.items():
    print(f"{key}: {value}")