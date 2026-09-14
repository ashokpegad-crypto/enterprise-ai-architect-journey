customers = [
    {
        "id": "CUST001",
        "name": "Ashok",
        "type": "Gold",
        "active": True
    },
    {
        "id": "CUST002",
        "name": "Ravi",
        "type": "Premium",
        "active": False
    },
    {
        "id": "CUST003",
        "name": "Priya",
        "type": "Silver",
        "active": True
    }
]

for customer in customers:
    print(f"Customer ID: {customer['id']}")
    print(f"Customer Name: {customer['name']}")
    print(f"Customer Type: {customer['type']}")
    print(f"Active: {customer['active']}")
    print("---")