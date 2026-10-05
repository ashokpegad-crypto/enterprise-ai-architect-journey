import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def process_employee():
    logger.info("Started employee processing")

    number = 10
    devider = 2
    return number / devider
try:
    result = process_employee()
    print(result)
except ZeroDivisionError:
    logger.exception("Employee processing failed")