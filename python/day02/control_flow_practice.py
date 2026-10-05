tickets = ["INC001", "INC002", "SKIP", "INC003", "STOP", "INC004"]

processed_count = 0

for ticket in tickets:
    if ticket == "SKIP":
        print(f"Skipping ticket: {ticket}")
        continue

    if ticket == "STOP":
        print("Stop signal received.")
        break

    print(f"Processing ticket: {ticket}")
    processed_count += 1

print(f"Total tickets processed: {processed_count}")