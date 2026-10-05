import unittest
from day13_api_client import Todo, TodoApiClient
import requests
from unittest.mock import Mock, patch


class TestTodoConversion(unittest.TestCase):
	def setUp(self):
		self.client = TodoApiClient("https://jsonplaceholder.typicode.com")

	def test_valid_api_data_converts_to_todo(self):
		api_data = {
			"userId": 1,
			"id": 101,
			"title": "Complete AI architecture study",
			"completed": True,
		}

		todo = TodoApiClient._to_todo(api_data)

		self.assertIsInstance(todo, Todo)
		self.assertEqual(todo.user_id, 1)
		self.assertEqual(todo.id, 101)
		self.assertEqual(todo.title, "Complete AI architecture study")
		self.assertTrue(todo.completed)

	def test_api_404_error(self):
		response = Mock()
		response.raise_for_status.side_effect = requests.exceptions.HTTPError
		with patch("day13_api_client.requests.get", return_value=response):
			with self.assertRaises(requests.exceptions.HTTPError):
				self.client._get("todos/1B")

	def test_api_500_error(self):
		response = Mock()
		response.raise_for_status.side_effect = requests.exceptions.HTTPError
		with patch("day13_api_client.requests.get", return_value=response):
			with self.assertRaises(requests.exceptions.HTTPError):
				self.client._get("todos/1")

	def test_api_invalid_json(self):
		response = Mock()
		response.raise_for_status.return_value = None
		response.json.side_effect = requests.exceptions.JSONDecodeError("Invalid JSON", "", 0)
		with patch("day13_api_client.requests.get", return_value=response):
			with self.assertRaises(requests.exceptions.JSONDecodeError):
				self.client._get("todos/1")

	def test_missing_fields(self):
		api_data = {
			"userId": 1,
			"id": 101,
			"completed": True
		}

		with self.assertRaises(KeyError):
			TodoApiClient._to_todo(api_data)

	def test_connection_error(self):
		"""Raise an exception when the connection fails."""
		with patch(
			"day13_api_client.requests.get",
			side_effect=requests.exceptions.ConnectionError("Connection failed"),
		):
			with self.assertRaises(requests.exceptions.ConnectionError):
				self.client._get("todos/1")

if __name__ == "__main__":
    unittest.main()

