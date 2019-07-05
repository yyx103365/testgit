
from libs.public_work import Logon
#添加教师类
class Add_teachers(Logon):
    def add_teacher(self,username,realname,password,sex,roleid,orid1,email,phone,location_p,location_c,location_a,address,introduce,type):

        url_addteacher='/admin.php?m=mgr/member2.saveMemberInfo&id='
        data_addteacher={
            'username':username,
            'realname':realname,
            'password':password,
            'sex':sex,
            'roleid':roleid,
            'orid1':orid1,
            'email':email,
            'phone':phone,
            'location_p':location_p,
            'location_c':location_c,
            'location_a':location_a,
            'address':address,
            'introduce':introduce,
            'type':type,

        }
        self.log_on('admin', 'admin')
        result_addteacher=self.http_request(url=url_addteacher,data=data_addteacher,cookies=self.cookies)
        return result_addteacher
if __name__ == '__main__':
        at=Add_teachers()
        a=at.add_teacher('18789099034','ftf','1346hjh','0','5','122','1233334@qq.com','18787876765','北京市','市辖区','东城区','jkjkj9jkk','ghjhjkkjk','1')
        # print(a.json())
        print(a.text)



