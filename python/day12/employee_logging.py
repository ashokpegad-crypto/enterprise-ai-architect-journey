from day10_employee_data_processing import employees, Employee
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def process_employee(employee):
    logger.info(
        f"Processing Employee {employee.employee_id} - "
        f"{employee.employee_name}"
    )

    if employee.assigned_cases >= 10:
        logger.warning(
            f"High workload for {employee.employee_id}: "
            f"{employee.assigned_cases} cases"
        )

    logger.info(
        f"Completed employee {employee.employee_id}"
    )

for employee in employees:
    process_employee(employee)