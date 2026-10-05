tickets = ["INC001", "INC002", "STOP", "INC003", "INC004"]

for ticket in tickets:
    if ticket == "STOP":
        print("Stop signal received. Ending processing.")
        break

    print(f"Processing ticket: {ticket}")

print("Ticket processing ended")