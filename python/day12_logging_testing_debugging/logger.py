import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

def process_employees():
    logger.info("Starting employee processing")
    logger.warning("High workload detected")
    logger.error("Employee processing failed")

process_employees()