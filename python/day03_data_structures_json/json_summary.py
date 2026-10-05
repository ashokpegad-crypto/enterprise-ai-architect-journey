import json

with open("customers.json", "r") as file:
    customers = json.load(file)

active_count = 0
inactive_count = 0
gold_count = 0
customer_type = set()

for customer in customers:
    if customer["active"]:
        active_count +=1
    else:
        inactive_count +=1
    if customer["customer_type"] == "Gold":
        gold_count +=1
    customer_type.add(customer["customer_type"])

summary = {
    "total_customers": len(customers),
    "active_customers": active_count,
    "inactive_customers": inactive_count,
    "gold_customers": gold_count,
    "unique_customer_types": len(customer_type)
}

print("Customer Summary:")
print("------------------")
print("Total Customers:", summary["total_customers"])
print("Active Customers:", summary["active_customers"])
print("Inactive Customers:", summary["inactive_customers"])
print("Gold Customers:", summary["gold_customers"])
print("Unique Customer Types:", summary["unique_customer_types"])

with open("customer_summary.json", "w") as file:
    json.dump(summary, file, indent=4)
    print("\nCustomer summary has been written to customer_summary.json")