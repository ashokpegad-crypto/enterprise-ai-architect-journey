customer_details = ( "CUST001", "Ashok", "Premium")
print("Original Customer Details:", customer_details)
try: 
    customer_details[1] = "Kumar"  # Attempting to modify the tuple
except TypeError as e:
    print("Tuples can not be modified after creation.")