import unittest
import logging


logger = logging.getLogger(__name__)


def process_employee(employee_id):
    logger.info(f"Processing employee {employee_id}")


class TestEmployeeLogging(unittest.TestCase):

    def test_processing_log(self):
        with self.assertLogs(logger, level="INFO") as captured:
            process_employee("EMP001")

        self.assertIn(
            "Processing employee EMP001",
            captured.output[0]
        )


if __name__ == "__main__":
    unittest.main()

