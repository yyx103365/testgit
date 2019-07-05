import requests
import unittest
import pymysql
import yagmail
import os
#  Http统一请求
class PublicClass(object):
    # host = 'http://192.168.1.32'

    host='http://localhost' #host  类变量
    # 这个方法，默认post方式，若需要用get来，则需要写明
    def http_request(self,url,method='post',*args,**kwargs):
        """

        :param url: 路径path
        :param method: 默认请求方式为post
        :param args:
        :param kwargs:
        :return:发起某个请求
        """
        url = '{}{}'.format(self.host, url)
        # 用.request方法封装，发起某个请求
        result = requests.request(method=method, url=url, *args, **kwargs)
        return result

# 校验类
class VerifyClass(unittest.TestCase):  #继承unittest
    # 校验状态码
    def verify_code(self,result,v_code):
        self.assertEqual(result.status_code,v_code)

    # 校验某个html字段
    def verify_html(self,result,v_html):
        # 包含某个字段存在文本中,注意，是包含，注意看一下参数
        self.assertIn(v_html,result.text)

    # 校验某个Json字段
    def verify_json(self,result,key,v_json):
        data = result.json().get(key)   #json要加一个括号，因为它是个字典啊
        self.assertEqual(data,v_json)

# 数据库的操作
def read_mysql_data(host,port,user,pwd,db,sql):
    """

    :param host: 域名
    :param port:数据库端口
    :param user:用户名
    :param pwd:密码
    :param db:数据库的库
    :param sql:sql语句
    :return:sql查询结果
    """
    # 建立sql连接对象
    conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db)
    # 生成游标对象
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 关闭游标
    cur.close()
    # 关闭数据库
    conn.close()
    # 查询sql结果
    data = cur.fetchone()
    return data

# 发送邮件
def send_email(user,pwd,port,body,subject,report,to_user,host='smtp.163.com',):
    '''
       :param user:发送者
       :param pwd:授权码
       :param port: https协议端口
       :param body:邮件内容
       :param subject:主题
       :param report:测试报告的附件
       :param to_user: 接受者账号，传入列表，默认是字符串，如果传多个请用列表的方式传递
       :param host:SMTP服务器地址
       :return:
       '''
    # 生成发送对象
    send = yagmail.SMTP(user=user, password=pwd, host=host, port=port)
    if type(to_user) is list:
        # 发送邮件
        send.send(to=to_user,subject=subject,contents=[body,report])
        flag = '发送给批量用户成功'
    elif type(to_user) is str:
        # 发送邮件
        send.send(to=to_user,subject=subject,contents=[body,report])
        flag = '发送给单个用户成功'
    else:
        flag = '发送数据错误'
    return flag
#测试结果的路径
FD = "./reports"

#获取发送最新的测试报告
# 导入os
def GetNewReport(FileDir=FD):
    # 打印目录所在所有文件名（列表对象）
    l = os.listdir(FileDir)
    # 按时间排序
    l.sort(key=lambda fn: os.path.getmtime(FileDir + "\\" + fn))
    # 获取最新的文件保存到file_new
    f = os.path.join(FileDir, l[-1])
    return f


