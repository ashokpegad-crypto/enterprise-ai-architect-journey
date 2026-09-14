import json

with open("customers.json", "r") as file:
    customers = json.load(file)

print("Gold Customers:")
gold_customers = []
for customer in customers:
    if customer["customer_type"] == "Gold":
        gold_customers.append(customer)
for customer in gold_customers:
    print(f"Customer ID: {customer['customer_id']} - {customer['customer_name']} - {customer['customer_type']}")
print("Total Gold Customers:", len(gold_customers))