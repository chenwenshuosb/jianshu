
import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)
handler=logging.FileHandler('hello.log',encoding='utf-8')
formater=logging.Formatter('%(asctime)s-%(message)s')
handler.setFormatter(formater)

logger.addHandler(handler)
logger.info('日志测试')