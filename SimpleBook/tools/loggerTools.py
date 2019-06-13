import logging
import os
import datetime

logFileName=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.txt'
from config import settings
class LogOption():
    def __init__(self):
        self.logName=os.path.join(settings.logPath,logFileName)
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.formater=logging.Formatter("%(asctime)s|%(filename)s|%(levelname)s:%(message)s")
        self.level='info'

    def logLevel(self,message):
        if message=='info':
            self.logger.info(message)
        if message=='debug':
            self.logger.debug(message)
        if message=='warning':
            self.logger.warning(message)
        if message=='error':
            self.logger.error(message)
    def writeLog(self,message):
        file=logging.FileHandler(self.logName,encoding='utf-8')
        file.setLevel(logging.INFO)
        file.setFormatter(self.formater)
        self.logger.addHandler(file)
        self.logLevel(message)
        # self.logger.removeHandler(file)
    def showConsole(self,message):
        console=logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(self.formater)
        self.logger.addHandler(console)
        self.logLevel(message)
        # self.logger.removeHandler(console)
    def printer(self,message):
        if settings.LOGWRITE:
            self.writeLog(message)
        if settings.LOGSHOW:
            self.showConsole(message)

