# Will's Media Server
# wms/__init__.py
# By William Neild

# Setup libraries
import sys
sys.path.insert(1, "./libraries/")

# grab all files/modules needed for wms
from wms.db import DB
from wms.config import Config
from wms.security import Security
from wms.server import Server
import logging, sys

# Setup logging to both file and terminal
file_handler = logging.FileHandler(filename='logs/main.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(
    level = logging.DEBUG,
    format = "[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt = "%d-%m-%Y %H:%M:%S",
    handlers = handlers
)

# Starting function
def start():
    logging.info("========== Starting Will's Media Server ==========")
    config = Config()
    Security(config)
    DB(config)
    Server(config)

# Stopping function
def stop():
    logging.info("========== Stopping Will's Media Server ==========")
