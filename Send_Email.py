'''

1.需要导入Python3标准库中的smtplib包和email包来实现邮件的构造和发送。

'''
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
# 处理图片需要 MIMEImage 类
from email.mime.image import MIMEImage

'''

2.配置邮件发送及接收人

'''
fromaddr = '1oo88@sina.cn'  # 邮件发送方邮箱地址
password = '******'  # 密码(部分邮箱为授权码)
toaddrs = ['1oo88@sina.cn', '1951995428@qq.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着可以写多个邮件地址群发

'''

3.内容

'''
# 邮件内容设置
message = MIMEText('Python发邮件测试', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = '测试'
# 发送方信息
message['From'] = fromaddr
# 接受方信息
message['To'] = toaddrs[0]

'''

4.登录并发送

'''
try:
    server = smtplib.SMTP('smtp.sina.cn')  # 163邮箱服务器地址，端口默认为25
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, message.as_string())
    print('success')
    server.quit()

except smtplib.SMTPException as e:
    print('error', e)  # 打印错误
