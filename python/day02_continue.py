tickets = ["INC001", "SKIP", "INC002", "INC003", "SKIP", "INC004"]

for ticket in tickets:
    if ticket == "SKIP":
        print("Skipping this ticket.")
        continue

    print(f"Processing ticket: {ticket}")

print("All eligible tickets processed")