def employee_status(active):
	if active:
		return "Active"
	return "Inactive"

result = employee_status(True)
print(result)