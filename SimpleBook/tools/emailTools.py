import os
import smtplib

from email.header import Header

from config import settings
from tools.reportTools import GetReport
from email.mime.text import MIMEText
report=GetReport()
reportFile=report.newReport()

class SendEmail():
    def __init__(self):
        self.sender=settings.sender
        self.receivcers=settings.receivers
        self.smtpServer=settings.smtpServer
        # if not settings.receivers:
        #     self.receivcers='xxxxxxxxx@qq.com'
    def getNewReport(self,reportFile):
        reportPath=os.path.join(settings.reportPath,reportFile)
        with open(reportPath,'rb') as fp:
            reportContent=fp.read()
        return reportContent

    def sendEmail(self,reportFile):
        content=self.getNewReport(reportFile)
        msg=MIMEText(content,'html','utf-8')
        msg['Subject']='简书登录自动化测试报告'
        msg['From']=Header('Mr.陈')
        msg['To']=Header('Mr.杨')

        server=smtplib.SMTP(settings.smtpServer,25)
        server.login(settings.sender,settings.passCode)

        try:
            server.sendmail(settings.sender,settings.receivers,msg.as_string())
            print('Eamil send OK,You are great')
        except Exception as e:
            print('Email send fail,You are loser')
