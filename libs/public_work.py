# conding=utf8
import requests
import json
from libs.tool import PublicClass
# 共享的登录函数
class Logon(PublicClass):
    cookies = {
        'PHPSESSID': ''
    }
    def log_on(self,username,password):
        # url 测试登录的接口
        url_logon = '/admin.php?m=mgr/admin.chklogin&ajax=1'
        # body传参
        data_logon = {
            'username': username,
            'password': password

        }
        # 这里是发送post请求，所以调用post_data方法，这里data=body，所以用icon==1，默认icon==1,所以可以不传，但icon=2的时候，就要传进来
        result_logon = self.http_request(url=url_logon, data=data_logon)
        # 获取登录的set_cookies，phpid的值
        data = result_logon.headers
        set_cookies = data['Set-Cookie']
        php_data = set_cookies.split('=')
        # print(php_data)
        # phpid = php_data[1].split(';')[0]
        phpid = php_data[3].split(';')[0]
        # print(phpid)
        self.cookies['PHPSESSID']=phpid
        # return phpid
        url_logon_success='/admin.php?m=mgr/admin.index_content'
        result_logon_success=self.http_request(method='get',url=url_logon_success,cookies=self.cookies)
        return result_logon_success
        # return result_logon


if __name__ == '__main__':

    lg=Logon()
    a=lg.log_on('admin','admin')

    # # jsdata = json.loads(a)
    # # print(jsdata)
    print(a.text)



