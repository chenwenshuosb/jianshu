from handles.inputer import InputerHandle

class RegisterStatus():
    def __init__(self,driver):
        self.input=InputerHandle(driver)

    #一触即发的执行设置
    def registerBegin(self,username,mobile,code,password):
        self.input.sendUsername(username)
        self.input.sendMobile(mobile)
        self.input.sendCode(code)
        self.input.sendPassword(password)
        self.input.clickButton()

    def isError(self):
        if self.input:
            return True
        return False