import json

employees=[
    {
        "employee_id": "EMP001",
        "employee_name": "Ashok",
        "department": "IT",
        "role": "Pega Developer",
        "active": True,
        "location": "Bangalore",
        "experience_years": 8,
        "assigned_cases": 12
    },
    {
        "employee_id": "EMP002",
        "employee_name": "Ravi",
        "department": "HR",
        "role": "HR Specialist",
        "active": False,
        "location": "Hyderabad",
        "experience_years": 5,
        "assigned_cases": 4
    },
    {
        "employee_id": "EMP003",
        "employee_name": "Priya",
        "department": "IT",
        "role": "Python Developer",
        "active": True,
        "location": "Chennai",
        "experience_years": 4,
        "assigned_cases": 9
    },
    {
        "employee_id": "EMP004",
        "employee_name": "Kiran",
        "department": "Finance",
        "role": "Financial Analyst",
        "active": True,
        "location": "Pune",
        "experience_years": 6,
        "assigned_cases": 7
    },
    {
        "employee_id": "EMP005",
        "employee_name": "Suresh",
        "department": "IT",
        "role": "System Architect",
        "active": False,
        "location": "Mumbai",
        "experience_years": 10,
        "assigned_cases": 15
    },
    {
        "employee_id": "EMP006",
        "employee_name": "Anil",
        "department": "HR",
        "role": "HR Manager",
        "active": True,
        "location": "Delhi",
        "experience_years": 9,
        "assigned_cases": 6
    }
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=7)

print("Employee data has been written to employees.json")

active_employees = 0
inactive_employees = 0
employee_department = {}
employee_departments = set()

with open("employees.json", "r") as file:
    loaded_employees = json.load(file)

    for employee in loaded_employees:
        if employee["active"]:
            active_employees += 1
        else:
            inactive_employees += 1

        department = employee["department"]
        employee_departments.add(department)
        if department in employee_department:
            employee_department[department] += 1
        else:
            employee_department[department] = 1

    assigned_cases_sum = sum(employee["assigned_cases"] for employee in loaded_employees)

print("\nEmployee Summary:")
print("------------------")
print("Total Employees:", len(loaded_employees))
print("Active Employees:", active_employees)
print("Inactive Employees:", inactive_employees)
print("Unique Departments:", len(employee_departments))
print("Employees by Department:")
for department, count in employee_department.items():
    print(f"  {department}: {count}")
print("Total Assigned Cases:", assigned_cases_sum)

with open("employee_summary.json", "w") as file:
    summary = {
        "total_employees": len(loaded_employees),
        "active_employees": active_employees,
        "inactive_employees": inactive_employees,
        "unique_departments": len(employee_departments),
        "employees_by_department": employee_department,
        "total_assigned_cases": assigned_cases_sum
    }
    json.dump(summary, file, indent=4)
    print("\nEmployee summary has been written to employee_summary.json")