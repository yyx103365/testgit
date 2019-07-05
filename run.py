import unittest
import time
import os
from HTMLTestReportCN import HTMLTestRunner
from libs.tool import (send_email,GetNewReport)
from config.configuration import (email_account,
email_pwd,
email_host,
email_port,
email_to_account)


def unitte_test():
    # 用unittest
    # discover方式来运行脚本
    dirpath = './scripts'
    discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
    currenttime = time.strftime('%y%m%d%H%M%S')
    filedir = './reports/' + 'report_' + currenttime + '.html'
    with open(filedir, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='添加教师接口测试报告',
                                description='edu平台接口测试报告',
                                tester="圆圆", verbosity=2)
        runner.run(discover)
    f = GetNewReport()
    send_email(user=email_account,pwd=email_pwd,host=email_host,port=email_port,to_user=email_to_account,
               subject='接口测试报告',body='领导，这是今天"edu添加教师"的接口报告',report=f)
    print('发送邮件成功')
if __name__ == '__main__':
    unitte_test()