from basepage.elementPosition import Position
from tools.loggerTools import LogOption
from tools.screenTools import ScreenShot
logger=LogOption()
screenShot=ScreenShot()
class InputerHandle():
    def __init__(self,driver):
        self.driver=driver
        self.position=Position(self.driver)

    def sendUsername(self,username):
        logger.writeLog('输入username:'+username)
        # screenPath=screenShot.savePic()
        self.position.getUsername().send_keys(username)
        # logger.showConsole(''.format(screenPath))
        # self.driver.save_screenshot(screenShot)
    def sendPassword(self,password):
        self.position.getPassword().send_keys(password)
    def sendMobile(self,mobile):
        self.position.getMobile().send_keys(mobile)
    def sendCode(self,code):
        self.position.getCode().send_keys(code)
    def clickButton(self):
        self.position.getRegButton().click()
    def usernameError(self):
        if self.position.getUsernameError():
            return False
        return True
