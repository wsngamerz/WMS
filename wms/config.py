import configparser, json, os, uuid, logging

class Config:

    configData = {}

    def __init__(self):
        logging.info("Initialising Config")
        if os.path.exists("config.ini") != True:
            self.createConfig()
        self.configData = self.loadConfig()


    def createConfig(self):
        logging.info("Creating config file")
        config = configparser.ConfigParser()
        config['General'] = {'fullname': 'Will\'s Media Server',
                             'shortname': 'WMS'}
        config['Server'] = {'hostname':'0.0.0.0',
                            'port':8080}
        config['Security'] = {'salt':str(uuid.uuid4())}
        with open("config.ini", "w") as configFile:
            config.write(configFile)

    def loadConfig(self):
        logging.info("Loading Config File")
        config = configparser.ConfigParser()
        config.read("config.ini")
        configData = json.loads(json.dumps(config._sections))
        logging.debug("Config File Data: " + str(configData))
        return configData
