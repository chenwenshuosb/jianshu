import configparser
import os

from config import settings

class ReadConfig():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.read=self.config.read(os.path.join(settings.configPath, 'config.ini'))
    def readValue(self,section,option):
        return self.config.get(section,option)


