import json

with open("customer.json", "r") as file:
    customer = json.load(file)

    print("Customer ID:", customer["customer_id"])
    print("Customer Name:", customer["customer_name"])
    print("Customer Type:", customer["customer_type"])
    print("Active:", customer["active"])
    print("Total Cases:", customer["total_cases"])
    print("Data Type of customer variable:", type(customer))