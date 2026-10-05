ticket = ["INC001", "INC002", "INC003", "INC004", "INC005"]
for ticket in ticket:
    if ticket == "INC003":
        continue  # Skip processing for ticket INC003
    print(f"Processing ticket: {ticket}")