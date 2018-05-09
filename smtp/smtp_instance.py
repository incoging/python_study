# coding=utf-8
# 这是一个SMTP(Sample mail transfer protocol)的简单例子

'''
专门注册了一个新浪邮箱
test1128@sina.com
yanjunqi
'''
# 创建smtp对象语法。
'''
import smtplib
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
    host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cc，这个是可选参数。
    port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
    local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。
Python SMTP对象使用sendmail方法发送邮件，语法如下：
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
    from_addr: 邮件发送者地址。
    to_addrs: 字符串列表，邮件发送地址。
    msg: 发送消息
这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 设置第三方SMTP服务器
# mail_host = "smtp.sina.com.cn"   #qq的服务器服务器
mail_host = "202.106.187.158"  # qq的服务器服务器
mail_user = "test1128@sina.com"
mail_pass = "yanjunqi"

sender = 'test1128@sina.com'  # 发送人
receivers = ['438506554@qq.com']  # 接收人

# 三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
message = MIMEText('python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = "Pythoon SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.connect(mail_host, 25)  # 465为QQ SMTP服务器的一个端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
