experience = int(input("Enter your years of experience: "))

if experience >= 10:
    print("Senior-level experience")
elif experience >= 5:
    print("Mid-level experience")
elif experience >= 2:
    print("Junior-level experience")
else:
    print("Entry-level experience")