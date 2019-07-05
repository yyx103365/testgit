import unittest
from po.add_teacher import Add_teachers
from libs.tool import VerifyClass
class TestAddteacher(VerifyClass):
    def setUp(self):
        self.ac = Add_teachers()
    def test_addteacher_001(self):
        result = self.ac.add_teacher('18789099023','ftf','1346hjh','0','5','122','1233334@qq.com','18787876765','北京市','市辖区','东城区','jkjkj9jkk','ghjhjkkjk','1')
        # self.verify_json(result, 'info', '保存成功')
        self.verify_html(result, '保存成功')
        self.verify_html(result, 'ok')
if __name__ == '__main__':
    unittest.main(verbosity=2)