import unittest
from libs.public_work import Logon
from libs.tool import VerifyClass

class TestSignin(VerifyClass):
    def setUp(self):
        self.lo=Logon()
    # 测试用例
    def test_signin_001(self):
        result=self.lo.log_on('admin','admin')
        self.verify_code(result,200)
        self.verify_html(result, '欢迎回来')
        self.verify_html(result, 'admin')
#
#
if __name__ == '__main__':
  unittest.main(verbosity=2)