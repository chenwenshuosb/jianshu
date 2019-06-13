import os

receivers = ["1758502069@qq.com"]
sender = '1135239005qq.com'
smtpServer = "smtp.qq.com"
passCode = "duthunlwzkotgiff"

#当前路径
basePath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#以当前路径为基础 拼接成config的路径
configPath=os.path.join(basePath,'config')
#以当前路径为基础 report
reportPath=os.path.join(basePath,'report')
#以当前路径为基础 logs
logPath=os.path.join(basePath,'logs')

screenPath=os.path.join(basePath,'report/screenshot')

LOGWRITE=True
LOGSHOW=True

