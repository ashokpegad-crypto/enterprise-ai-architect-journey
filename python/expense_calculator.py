income = float(input("Monthly income: "))
rent = float(input("Rent: "))
food = float(input("Food: "))
travel = float(input("Travel: "))
other = float(input("Other expenses: "))

total_expenses = rent + food + travel + other
remaining = income - total_expenses
savings_percentage = (remaining / income) * 100 if income != 0 else 0

print(f"\nTotal expenses: ₹{total_expenses:,.2f}")
print(f"Remaining income: ₹{remaining:,.2f}")
print(f"Savings percentage: {savings_percentage:.2f}%")