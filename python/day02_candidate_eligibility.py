name = input("Enter candidate name: ")
experience = int(input("Enter years of experience: "))

has_python_skill = input("Does the candidate know Python? (yes/no): ").strip().lower()
while has_python_skill not in ("yes", "no"):
    print("Invalid input. Please answer yes or no.")
    has_python_skill = input("Does the candidate know Python? (yes/no): ").strip().lower()

has_api_skill = input("Does the candidate know APIs? (yes/no): ").strip().lower()
while has_api_skill not in ("yes", "no"):
    print("Invalid input. Please answer yes or no.")
    has_api_skill = input("Does the candidate know APIs? (yes/no): ").strip().lower()

if experience >= 2 and has_python_skill == "yes" and has_api_skill == "yes":
    print(f"{name} is eligible for technical screening.")
elif experience >= 2 and (has_python_skill == "yes" or has_api_skill == "yes"):
    print(f"{name} has relevant experience but needs additional skill development.")
else:
    print(f"{name} is not currently eligible for technical screening.")