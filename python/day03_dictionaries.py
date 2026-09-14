customer = {
    "id": "CUST001",
    "name": "Ashok",
    "type": "Premium",
    "active": True
}

print("Customer Details:", customer)
print("Customer ID:", customer["id"])
print("Customer Name:", customer["name"])
print("Customer Type:", customer["type"])  
print("Customer Active:", customer["active"])

customer["city"] = "Bangalore"
print("After adding city:", customer)  

customer["type"] = "Gold"
print("After updating type:", customer)

print("Total customer attributes:", len(customer))
print("Customer keys:", customer.keys())
print("Customer values:", customer.values())