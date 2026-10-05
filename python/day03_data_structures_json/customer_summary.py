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

active_count = 0
gold_count = 0
inactive_count = 0

for customer in customers:
    if customer["active"]:
        active_count += 1

    else:
        inactive_count += 1
    if customer["type"] == "Gold":
            gold_count += 1

print("Customer Summary:")
print("-----------------")
print(f"Total customers: {len(customers)}")
print(f"Active customers: {active_count}")
print(f"Inactive customers: {inactive_count}")
print(f"Gold customers: {gold_count}")