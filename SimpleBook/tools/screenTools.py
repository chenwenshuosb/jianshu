import datetime
import os
from config.settings import screenPath
class ScreenShot():
    def savePic(self):
        screenshotPath=screenPath
        screenshotName=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".png"
        return os.path.join(screenPath,screenshotName)