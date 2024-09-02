import logging
import os


from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(os.getcwd(),log_dir,LOG_FILE)
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(filename=logs_path, style='{',format="{asctime} - {levelname} - {message}", level=logging.DEBUG)