from dataclasses import dataclass
import logging
from day13_api_client import Todo, TodoApiClient
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

@dataclass
class Employee:
    employee_id: str
    name: str
    user_id: int

def get_employee_summary(employee: Employee, client: TodoApiClient) -> dict[str, str | int | bool]:
    try:
        todos = client.get_todos_by_user(employee.user_id)
        completed_todos = [todo for todo in todos if todo.completed]
        pending_todos = [todo for todo in todos if not todo.completed]
        completed_percentage = (len(completed_todos) / len(todos)) * 100 if todos else 0
        return {
            "employee_id": employee.employee_id,
            "name": employee.name,
            "Total Todos": len(todos),
            "Completed Todos": len(completed_todos),
            "Pending Todos": len(pending_todos),
            "Completed Percentage": completed_percentage
        }
    except RequestException as error:
        logger.error(f"Failed to fetch todos for user {employee.user_id}: {error}")
        return {
            "employee_id": employee.employee_id,
            "name": employee.name,
            "Total Todos": 0,
            "Completed Todos": 0,
            "Pending Todos": 0,
            "Completed Percentage": 0
        }

def generate_employee_summaries(employees: list[Employee], client: TodoApiClient) -> list[dict[str, str | int | bool]]:
    summaries = []
    for employee in employees:
        logger.info(f"Generating summary for employee {employee.name} (ID: {employee.employee_id})")
        summary = get_employee_summary(employee, client)
        summaries.append(summary)
    return summaries

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting Employee Todo Summary Generation")
    employee1 = Employee("EMP001", "Ashok", 1)
    employee2 = Employee("EMP002", "Ravi", 2)
    employee3 = Employee("EMP003", "Priya", 3)
    employees = [employee1, employee2, employee3]
    client = TodoApiClient("https://jsonplaceholder.typicode.com")
    summaries = generate_employee_summaries(employees, client)
    for summary in summaries:
        print(f"Employee Name: {summary['name']}")
        print(f"Employee ID: {summary['employee_id']}")
        print(f"Total Todos: {summary['Total Todos']}")
        print(f"Completed Todos: {summary['Completed Todos']}")
        print(f"Pending Todos: {summary['Pending Todos']}")
        print(f"Completed Percentage: {summary['Completed Percentage']:.2f}%")
        print("")

if __name__ == "__main__":
    main()
    