answer = input("Does the candidate know Python? (yes/no): ").strip().lower()

if answer == "yes":
    print("Python skill confirmed.")
elif answer == "no":
    print("Python skill not confirmed.")
else:
    print("Invalid input. Please enter yes or no.")