# Will's Media Server
# wms/__init__.py
# By William Neild

# Setup libraries
from flask import Flask
import sys, os
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

# Check whether folders exist
directories = ["logs/", "libraries/", "wms/"]
directoryErrors = 0
logging.info("Checking for required folders")
for directory in directories:
    logging.debug("checking for " + directory)
    if os.path.isdir(directory) != True:
        directoryErrors+=1
        logging.error(directory + " is missing")

if directoryErrors > 0:
    logging.info("Stoping Server due to Errors")
    sys.exit()
else:
    logging.info("All folders found")

# Initialise flask
app = Flask(__name__)

# Starting function
def start():
    logging.info("========== Starting Will's Media Server ==========")
    config = Config()
    security = Security(app, config)
    db = DB(app, config)
    server = Server(app, config)

# Stopping function
def stop():
    logging.info("========== Stopping Will's Media Server ==========")
