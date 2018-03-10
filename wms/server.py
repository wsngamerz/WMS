import logging, random
from wms import config, db, routes

class Server:
    def __init__(self, app, config):
        logging.info("Initialising Server")
        self.configData = config.configData
        self.runServer(app)

    def runServer(self, app):
        app.secret_key = self.configData["Security"]["salt"]
        app.run(self.configData["Server"]["hostname"], int(self.configData["Server"]["port"]))
