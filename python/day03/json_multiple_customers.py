import json

customers = [
    {
        "customer_id": "CUST001",
        "customer_name": "Ashok",
        "customer_type": "Gold",
        "active": True,
        "total_cases": 5
    },
    {
        "customer_id": "CUST002",
        "customer_name": "Ravi",
        "customer_type": "Premium",
        "active": False,
        "total_cases": 3
    },
    {
        "customer_id": "CUST003",
        "customer_name": "Priya",
        "customer_type": "Gold",
        "active": True,
        "total_cases": 8
    }
]

with open("customers.json", "w") as file:
    json.dump(customers, file, indent=4)

    print("Customer data has been written to customers.json")
with open("customers.json", "r") as file:
    loaded_customers = json.load(file)
    print("\n Customer Details")

    for customer in loaded_customers:
        print(f"{customer["customer_id"]} -"
              f"{customer["customer_name"]} -"
              f"{customer["customer_type"]} -"
              f"{customer["active"]}")
        
print("\nTotal Customers:", len(loaded_customers)) 
print("Data Type", type(loaded_customers)) # Print a blank line between customers