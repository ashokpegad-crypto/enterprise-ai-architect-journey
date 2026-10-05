tickets = [
    {"id": "INC001", "priority": "high", "status": "open"},
    {"id": "INC002", "priority": "low", "status": "open"},
    {"id": "INC003", "priority": "medium", "status": "closed"},
    {"id": "INC004", "priority": "high", "status": "open"},
    {"id": "INC005", "priority": "low", "status": "closed"},
]

processed_count = 0

for ticket in tickets:
    if ticket["status"] == "closed":
        print(f"Skipping closed ticket: {ticket['id']}")
        continue

    if ticket["priority"] == "high":
        print(f"Urgent processing required: {ticket['id']}")
    else:
        print(f"Processing ticket: {ticket['id']}")

    processed_count += 1

print(f"Total open tickets processed: {processed_count}")