from tools.readConfig import ReadConfig

class FindElement():
    def __init__(self,driver):
        self.driver=driver
    def getElment(self,section,option):
        read=ReadConfig()
        data=read.readValue(section,option)
        by,value=data.split('|')
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            if by=='xpath':
                return self.driver.find_element_by_xpath(value)
            if by=='class':
                return self.driver.find_element_by_class_name(value)
            if by=='css':
                return self.driver.find_element_by_css(value)
        except Exception:
            return None