customer_ids = {"CUST001", "CUST002", "CUST003", "CUST001"}

print("Customer IDs:", customer_ids)
print("Total unique customer IDs:", len(customer_ids))

customer_ids.add("CUST004")
print("After adding a new customer ID:", customer_ids)

customer_ids.remove("CUST002")
print("After removing a customer ID:", customer_ids)