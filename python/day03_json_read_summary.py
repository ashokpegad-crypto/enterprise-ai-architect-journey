import json

with open("customer_summary.json", "r") as file:
    summary = json.load(file)

print("Loaded Customer Summary")
print("-----------------------")
print("Total Customers:", summary["total_customers"])
print("Active Customers:", summary["active_customers"])
print("Inactive Customers:", summary["inactive_customers"])
print("Gold Customers:", summary["gold_customers"])
print("Unique Customer Types:", summary["unique_customer_types"])