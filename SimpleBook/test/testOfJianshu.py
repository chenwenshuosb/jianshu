import os
import unittest
from tools import HTMLTestRunner
import ddt
from config import settings
from tools.loggerTools import LogOption
from selenium import webdriver
from readyTest.readOver import RegisterStatus
from handles.inputer import InputerHandle
from tools.emailTools import SendEmail
from tools.reportTools import GetReport
import datetime


logger=LogOption()
@ddt.ddt
class CaseOfJianshu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.jianshu.com/sign_up')
        self.driver.refresh()
        self.driver.maximize_window()
        self.carry=RegisterStatus(self.driver)
        self.driver.implicitly_wait(5)
    def tearDown(self):
        for methodName,error in self._outcome.errors:
            if error:
                caseName = self._testMethodName
                errorPng=caseName+'.png'
                pngPath=os.path.join(settings.screenPath,errorPng)
                self.driver.save_screenshot(pngPath)

        self.driver.quit()
    @ddt.data(
        ('cws1135239005','17600035024','xxxx','ccc123456'),
        ('cws','17600035024','xxxx','ccc123456')
    )
    @ddt.unpack
    def testRegister(self,*data):
        username,mobile,code,password=data
        register=RegisterStatus(self.driver)
        register.registerBegin(username,mobile,code,password)
        logger.writeLog('info')
        # self.assertFalse(self.carry.isError())

def run():
    suite=unittest.TestLoader().loadTestsFromTestCase(CaseOfJianshu)
    reportName = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".html"
    reportPath = os.path.join(settings.reportPath, reportName)
    with open(reportPath, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='简书测试报告')
        runner.run(suite)

    report = GetReport()
    reportFile = report.newReport()  # 获取最近一次报告
    sendEmail = SendEmail()  # 发送邮件
    sendEmail.sendEmail(reportFile)