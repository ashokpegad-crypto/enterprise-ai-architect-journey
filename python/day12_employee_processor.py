import logging
from dataclasses import dataclass


logging.basicConfig(
    level=logging.INFO,
    filename="employee_processor.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)


@dataclass
class Employee:
    employee_id: str
    employee_name: str
    department: str
    active: bool
    experience_years: int
    assigned_cases: int


def validate_employee(employee):
    if not employee.employee_id:
        raise ValueError("Employee ID is required")

    if not employee.employee_name:
        raise ValueError("Employee name is required")

    if employee.experience_years < 0:
        raise ValueError("Experience cannot be negative")

    if employee.assigned_cases < 0:
        raise ValueError("Assigned cases cannot be negative")

    return True


def get_active_employee_names(employees):
    return [employee.employee_name for employee in employees if employee.active]


def get_high_workload_employee_names(employees):
    return [
        employee.employee_name
        for employee in employees
        if employee.assigned_cases >= 10
    ]


def process_employees(employees):
    logger.info("Employee processing started")

    try:
        for employee in employees:
            validate_employee(employee)
            logger.info(
                "Processing employee %s - %s",
                employee.employee_id,
                employee.employee_name,
            )
            if employee.assigned_cases >= 10:
                logger.warning("High workload for %s", employee.employee_id)
    except Exception:
        logger.exception("Employee processing failed")
        raise

    logger.info("Employee processing completed")


def build_employee_summary(employees):
    employees = list(employees)
    active_count = sum(1 for employee in employees if employee.active)
    high_workload_count = sum(
        1 for employee in employees if employee.assigned_cases >= 10
    )

    return (
        f"Total Employees: {len(employees)}\n"
        f"Active Employees: {active_count}\n"
        f"High Workload Employees: {high_workload_count}"
    )


if __name__ == "__main__":
    employees = [
        Employee("EMP001", "Ashok", "IT", True, 8, 12),
        Employee("EMP002", "Ravi", "HR", False, 5, 4),
        Employee("EMP003", "Priya", "IT", True, 4, 9),
        Employee("EMP004", "Kiran", "Finance", True, 6, 15),
        Employee("EMP005", "Anil", "IT", False, 7, 11),
    ]

    process_employees(employees)
    print(f"Active Employees: {get_active_employee_names(employees)}")
    print(f"High Workload Employees: {get_high_workload_employee_names(employees)}")
    print(build_employee_summary(employees))