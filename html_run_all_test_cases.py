import os
import smtplib
import unittest
#htmltestrunner 是基于unittest框架的一个扩展，可以在网上下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path, 'rb')
    #read()读取全部
    mail_body = f.read()#读取html报告的内容，作为邮件的正文
    #f.readline()一行一行的读
    f.close()
    #要想发邮件，我们要把二进制的内容转成MIME
    #MIME multipurpose多用途 internet互联网 mail 邮件 extension 扩展
    #这种格式是对邮件协议的一个扩展，使邮件不仅支持文本格式，还支持多种格式，比如图片，音频，二进制文件

   # MIMEText(mail_body,'html','utf-8')#类型转换
#赋值
    msg = MIMEText(mail_body, 'html', 'utf-8')
    #上面的邮件的正文，但是对于一个邮件来讲，除了正文，还需要主题，发件人，收件人
    #msg是字典的类型，字典类似于数组：区别：1.字典是无序的
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    #如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮件，需要单独设置一个客户端授权码
    #为了邮箱安全着想
    #因为你们没有设置授权码，所以发件箱统一用我的
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = '742303846@qq.com'

    #现在邮件内容已经准备好了，下面开始发送邮件
    #发邮件的手动步骤
    #1.打开登录页面，连接邮箱服务器
    #要想连接服务器，首先必须搞清楚网络传输协议
    #http,https,ftp,socket
    #发邮件的协议，一般有三种，你要先查看你的邮箱支持那种协议
    #126邮箱支持这三种协议，pop3,smtp,imap
    #我们要选一种传输协议，用来发邮件，smtp
    #smtp simple mail transfer ,protocol简单传输协议
    #首先导入smtplib的代码库
    smtp = smtplib.SMTP()
    #实例化一个SMTP类对象
    smtp.connect("smtp.126.com")#链接126邮箱的服务器地址
    #2.登录邮箱
    #smtp.login('bwftest126@126.com', 'abc123asd654')
    smtp.login('liuxiaoqianabc@126.com', 'lxq450851')
    #使用授权码作为密码登录
    #3.发送邮件
    #smtp.sendmail(from_addr, to_addrs, msg, mail_options=[],
        #         rcpt_options=[])
    #注意msg是MIME类型，需要转成string类型再发送
    smtp.sendmail('liuxiaoqianabc@126.com', '742303846@qq.com', msg.as_string())
    #smtp.sendmail('bwftest126@126.com', 'liuxiaoqianabc@126.com', msg.as_string())
    #smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    #4.退出邮箱
    smtp.quit()
    print("email has sent out")


if __name__ == '__main__':
    #加入时间戳
    #定义一个变量now
    #str是string f是format格式,strftime格式化的时间
    #strftime()通过这个方法可以定义时间格式
    #Y year年，m month 月，d day天，H hour时，M minute 分，S second秒
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./day5', '*Test.py')
    #unittest.TextTestRunner()文本测试用例运行器
    #现在用htmltestrunner测试用例运行器
    #html的测试用例运行器最终会生成一个html格式的测试报告
    #我们是不是至少要指定测试报告的路径
    #sys.stdout系统标准输出steady
    base_path = os.path.dirname(__file__)
    #report.html文件名,b：binarycode二进制标准文件
    #path = base_path + "./report/report.html"
    path = base_path + "./report/report" + now + ".html"
    file = open(path, 'wb')
    # def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None):
    #默认值可以不写值
    #HTMLTestRunner(stream=file, title="海盗商城测试报告", description="测试环境：window server 2008 +Chro"
               #                                               "me").run(suite)
    HTMLTestRunner(file, 1, title="海盗商城测试报告", description="测试环境：window server 2008 +Chro"
                                                              "me").run(suite)
    file.close()
    #我们要把html报告作为邮件正文，发送邮件
    send_mail(path)
#这时生成的测试报告，只显示类名和方法名，只能给专业的人士看
#我们应该相关的手动测试用例的标题加到我们的测试报告
#我们自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写我们就怎么编写代码
#所以我们的代码里应该可以体现手工测试用例的标题
#新的测试报告会覆盖原来的测试报告，如果想把所有的测试报告怎么保存起来，编写为不同的文件名
#加一个时间戳，按照当前时间计算一个数字，把数字作为文件
    # 名的一部分，那么就避免了文件名重复的问题
    #现在我们的html格式的测试报告生成了，当测试用例全部执行完成，我们应该生成一封邮件提醒，通知所有关心测试结果的人
