tickets = ["INC001", "INC002", "INC003"]
print("All tickets:", tickets)
print("First ticket:", tickets[0])
print("Second ticket:", tickets[1])

tickets.append("INC004")
print("After adding ticket:", tickets)

tickets.remove("INC002")
print("After removing ticket:", tickets)

print("Total tickets:", len(tickets))