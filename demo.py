from us_visa.logger import logging
from us_visa.execption import USvisaException

logging.info("Welcome to our custome log")

try:
    a = 1/"10"
except Exception as e:
    logging.info(e)
    raise USvisaException("Error occurred: ", e) from e