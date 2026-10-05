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
        "type": "Gold",
        "active": True
    },
    {
        "id": "CUST004",
        "name": "Kiran",
        "type": "Silver",
        "active": True
    }
]

gold_customers = []

for customer in customers:
    if customer["type"] == "Gold" and customer["active"]:
        gold_customers.append(customer)

print("Gold Customers:")
for customer in gold_customers:
    print(f"Customer ID: {customer['id']} - {customer['name']} - {customer['type']}")
print("Total gold customers:", len(gold_customers))