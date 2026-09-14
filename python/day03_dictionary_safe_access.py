customer = {
    "id": "CUST001",
    "name": "Ashok",
    "type": "Gold",
    "email": input("Enter customer email: ").strip()
}

print("Customer ID:", customer.get("id"))
print("Customer Email:", customer.get("email"))

print("Customer Email with default:", customer.get("email", "Not provided"))