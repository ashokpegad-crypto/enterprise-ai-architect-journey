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

active_customers = []

for customer in customers:
    if customer["active"]:
        active_customers.append(customer)

print("Active Customers:")
for customer in active_customers:
    print(f"Customer ID: {customer['id']} - {customer['name']} - {customer['type']}")
print("Total active customers:", len(active_customers))