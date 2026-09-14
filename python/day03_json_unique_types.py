import json

with open("customers.json", "r") as file:
    customers = json.load(file)

customer_type = set()

for customer in customers:
    customer_type.add(customer["customer_type"])
print("Unique Customer Types:", customer_type)
print("Total Unique Customer Types:", len(customer_type))