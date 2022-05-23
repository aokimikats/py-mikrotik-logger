import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('server_config.ini')

        self.filename = self.config['LOGS']['LOG_FILENAME']
        self.dir = self.config['LOGS']['LOG_DIR']

        self.host = self.config['ROUTING']['HOST']
        self.port = int(self.config['ROUTING']['PORT'])
        self.timeout = self.config['ROUTING']['TIMEOUT']
