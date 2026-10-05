import requests
from dataclasses import dataclass
from typing import Any

@dataclass
class Todo:
    user_id: int
    id: int
    title: str
    completed: bool

class TodoApiClient:
	def __init__(self, base_url: str) -> None:
		self.base_url = base_url.rstrip("/")

	def _get(
		self,
		endpoint: str,
		params: dict[str, int] | None = None,
	) -> Any:
		url = f"{self.base_url}/{endpoint.lstrip('/')}"
		response = requests.get(url, params=params)
		response.raise_for_status()
		return response.json()

	@staticmethod
	def _to_todo(data: dict[str, Any]) -> Todo:
		return Todo(
			user_id=data["userId"],
			id=data["id"],
			title=data["title"],
			completed=data["completed"],
		)

	def get_todo(self, todo_id: int) -> Todo:
		return self._to_todo(self._get(f"todos/{todo_id}"))

	def get_all_todos(self) -> list[Todo]:
		data = self._get("todos")
		return [self._to_todo(item) for item in data]

	def get_todos_by_user(self, user_id: int) -> list[Todo]:
		data = self._get("todos", params={"userId": user_id})
		return [self._to_todo(item) for item in data]


def main() -> None:
	client = TodoApiClient("https://jsonplaceholder.typicode.com")
	todo = client.get_todo(1)
	todos = client.get_all_todos()
	todos_by_user = client.get_todos_by_user(1)

	print(f"Total Todos: {len(todos)}")
	print(f"First Todo ID: {todo.id}")
	print(f"First Todo Title: {todo.title}")
	print(f"First Todo Completed: {todo.completed}")
	print()
	print(f"Todos for User 1: {len(todos_by_user)}")


if __name__ == "__main__":
	main()
