# Will's Media Server
# wms/__init__.py
# By William Neild

# Setup libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys, os
sys.path.insert(1, "./libs/")

# grab all files/modules needed for wms
from wms.db import DB
from wms.db import db
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
directories = ["logs/", "libs/", "wms/"]
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

# configure sqlalchemy withy flask
app.config["SQLALCHEMY_DATABASE_URI"] = str("sqlite:///" + os.path.join(os.getcwd(), "database", "main.db"))
app.config["SQLALCHEMY_BINDS"] = {
    "users": str('sqlite:///' + os.path.join(os.getcwd(), "database", "users.db")),
    "music": str('sqlite:///' + os.path.join(os.getcwd(), "database", "libraries", "music.db")),
    "films": str('sqlite:///' + os.path.join(os.getcwd(), "database", "libraries", "films.db")),
    "tv": str('sqlite:///' + os.path.join(os.getcwd(), "database", "libraries", "tv.db"))
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Load Required core config
config = Config()
database = DB(config)
security = Security(config)

# Add all flask views
from .views import home, dashboard, music, films, tv
homeBlueprint = home.homeBlueprint(config, database, security)

# Register Flask Blueprints
app.register_blueprint(homeBlueprint.home)

# TODO: Implement These below
# app.register_blueprint(dashboard)
# app.register_blueprint(music)
# app.register_blueprint(films)
# app.register_blueprint(tv)

# Initialise SQLAlchemy Databases
db.init_app(app)
db.create_all(app=app)

# Starting function
def start():
    logging.info("========== Starting Will's Media Server ==========")
    server = Server(app, config)

# Stopping function
def stop():
    logging.info("========== Stopping Will's Media Server ==========")
