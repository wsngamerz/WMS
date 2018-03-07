from flask import Flask
import logging, random
from wms import config, db

app = Flask(__name__)
from wms import routes

class Server:
    def __init__(self, config):
        logging.info("Initialising Server")
        self.configData = config.configData
        routes.Routes(app, config.configData)
        self.runServer()

    def runServer(self):
        app.secret_key = self.configData["Security"]["salt"]
        app.run(self.configData["Server"]["hostname"], int(self.configData["Server"]["port"]))
