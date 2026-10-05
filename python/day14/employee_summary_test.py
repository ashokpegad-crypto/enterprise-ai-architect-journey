import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, call, patch

from requests.exceptions import RequestException

sys.path.insert(0, str(Path(__file__).resolve().parent))

from day13_api_client import Todo, TodoApiClient
from day14_employee_todo_integration import (
	Employee,
	generate_employee_summaries,
	get_employee_summary,
)


class TestEmployeeSummary(unittest.TestCase):
	def setUp(self):
		self.http_get_patcher = patch("day13_api_client.requests.get")
		self.mock_http_get = self.http_get_patcher.start()
		self.addCleanup(self.http_get_patcher.stop)

	def tearDown(self):
		self.mock_http_get.assert_not_called()

	def test_successful_employee_summary(self):
		employee = Employee("EMP001", "Ashok", 1)
		todos = [
			Todo(1, 101, "Task 1", True),
			Todo(1, 102, "Task 2", True),
			Todo(1, 103, "Task 3", False),
			Todo(1, 104, "Task 4", False),
		]
		client = Mock(spec=TodoApiClient)
		client.get_todos_by_user.return_value = todos

		summary = get_employee_summary(employee, client)

		self.assertEqual(summary["employee_id"], "EMP001")
		self.assertEqual(summary["name"], "Ashok")
		self.assertEqual(summary["Total Todos"], 4)
		self.assertEqual(summary["Completed Todos"], 2)
		self.assertEqual(summary["Pending Todos"], 2)
		self.assertEqual(summary["Completed Percentage"], 50)

	def test_api_client_called_with_correct_user_id(self):
		employee = Employee("EMP001", "Ashok", 1)
		client = Mock(spec=TodoApiClient)
		client.get_todos_by_user.return_value = []

		get_employee_summary(employee, client)

		client.get_todos_by_user.assert_called_once_with(1)

	def test_api_failure_returns_fallback(self):
		employee = Employee("EMP002", "Ravi", 2)
		client = Mock(spec=TodoApiClient)
		client.get_todos_by_user.side_effect = RequestException("API unavailable")

		summary = get_employee_summary(employee, client)

		self.assertEqual(summary["employee_id"], "EMP002")
		self.assertEqual(summary["name"], "Ravi")
		self.assertEqual(summary["Total Todos"], 0)
		self.assertEqual(summary["Completed Todos"], 0)
		self.assertEqual(summary["Pending Todos"], 0)
		self.assertEqual(summary["Completed Percentage"], 0)

	def test_multiple_employee_summaries(self):
		employees = [
			Employee("EMP001", "Ashok", 1),
			Employee("EMP002", "Ravi", 2),
			Employee("EMP003", "Priya", 3),
		]
		client = Mock(spec=TodoApiClient)
		client.get_todos_by_user.side_effect = [
			[
				Todo(1, 101, "Task 1", True),
				Todo(1, 102, "Task 2", True),
				Todo(1, 103, "Task 3", False),
				Todo(1, 104, "Task 4", False),
			],
			[
				Todo(2, 201, "Task 1", True),
				Todo(2, 202, "Task 2", False),
				Todo(2, 203, "Task 3", False),
			],
			[
				Todo(3, 301, "Task 1", True),
				Todo(3, 302, "Task 2", True),
			],
		]

		summaries = generate_employee_summaries(employees, client)

		self.assertEqual(len(summaries), 3)
		self.assertEqual(client.get_todos_by_user.call_args_list, [call(1), call(2), call(3)])
		self.assertEqual([summary["Total Todos"] for summary in summaries], [4, 3, 2])
		self.assertEqual([summary["Completed Todos"] for summary in summaries], [2, 1, 2])
		self.assertEqual([summary["Pending Todos"] for summary in summaries], [2, 2, 0])
		self.assertEqual(summaries[0]["Completed Percentage"], 50)
		self.assertAlmostEqual(summaries[1]["Completed Percentage"], 33.33, places=2)
		self.assertEqual(summaries[2]["Completed Percentage"], 100)

	def test_empty_todo_list(self):
		employee = Employee("EMP003", "Priya", 3)
		client = Mock(spec=TodoApiClient)
		client.get_todos_by_user.return_value = []

		summary = get_employee_summary(employee, client)

		self.assertEqual(summary["Total Todos"], 0)
		self.assertEqual(summary["Completed Todos"], 0)
		self.assertEqual(summary["Pending Todos"], 0)
		self.assertEqual(summary["Completed Percentage"], 0)


if __name__ == "__main__":
	unittest.main()
