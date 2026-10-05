pega_users = {"Ashok", "Ravi", "Suresh", "Priya"}
python_users = {"Ashok", "Priya", "Kiran", "Anil"}

print("Pega Users:", pega_users)
print("Python Users:", python_users)

print("Users who know both Pega and Python:", pega_users & python_users)
print("Users who know either Pega or Python:", pega_users | python_users)
print("Users who know only Pega:", pega_users - python_users)
print("Users who have one skill :", python_users ^ pega_users)