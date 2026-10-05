from day10_employee_data_processing import Employee, employees
from day11_contextlib_timer import execution_timer
from day11_log_execution import log_execution


@log_execution
def process_employees(employees: list[Employee]) -> None:
	with execution_timer("employee processing"):
		active_employees = [employee.employee_name for employee in employees if employee.active]
		high_workload_employees = (
			employee for employee in employees if employee.assigned_cases >= 10
		)

		print(f"Active Employees: {active_employees}")
		print()
		print("High Workload Employees:")
		for employee in high_workload_employees:
			print(f"{employee.employee_name} - {employee.assigned_cases}")


if __name__ == "__main__":
	process_employees(employees)
