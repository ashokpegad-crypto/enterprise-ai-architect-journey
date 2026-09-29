import logging

logging.basicConfig(
    level=logging.INFO,
    filename="employee_processor.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)

def process_employees():
    logger.info("Employee processing started")
    logger.warning("High workload detected")
    logger.error("Employee processing failed")

process_employees()