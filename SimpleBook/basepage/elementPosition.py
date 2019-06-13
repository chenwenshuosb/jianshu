from middleware.findElment import FindElement

class Position():

    def __init__(self,driver):
        self.find=FindElement(driver)

    def getUsername(self):
        return self.find.getElment('register','username')

    def getPassword(self):
        return self.find.getElment('register','password')

    def getMobile(self):
        return self.find.getElment('register','mobile')

    def getCode(self):
        return self.find.getElment('register','code')

    def getRegButton(self):
        return self.find.getElment('register','reg')

    def getUsernameError(self):
        return self.find.getElment('register','usernameError')