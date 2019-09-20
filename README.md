# Python_sendEmail
使用Python内置的smtplib包和email包来实现邮件的构造和发送。

# 发送纯文本时：

## 1.需要导入Python3标准库中的smtplib包和email包来实现邮件的构造和发送。

```python
import smtplib

# 发送字符串的邮件

from email.mime.text import MIMEText

# 处理多种形态的邮件主体需要 MIMEMultipart 类

from email.mime.multipart import MIMEMultipart

# 处理图片需要 MIMEImage 类

from email.mime.image import MIMEImage
```







## 2.配置邮件发送及接收人

```python
fromaddr = '1oo88@sina.cn'  # 邮件发送方邮箱地址
password = '******'  # 密码(部分邮箱为授权码)
toaddrs = ['1oo88@sina.cn', '1951995428@qq.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着可以写多个邮件地址群发
```







## 3.内容


```python
#邮件内容设置

message = MIMEText('Python发邮件测试', 'plain', 'utf-8')

#邮件主题

message['Subject'] = '测试'

#发送方信息

message['From'] = fromaddr

#接受方信息

message['To'] = toaddrs[0]
```







## 4.登录并发送

```python
try:
    server = smtplib.SMTP('smtp.sina.cn')  # 163邮箱服务器地址，端口默认为25
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, message.as_string())
    print('success')
    server.quit()

except smtplib.SMTPException as e:
    print('error', e)  # 打印错误
```



# 发送带有附件时：



## 1.设置email信息

```python
#添加一个MIMEmultipart类，处理正文及附件
message = MIMEMultipart()
message['From'] = fromaddr
message['To'] = toaddrs[0]
message['Subject'] = 'title'
```

***推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等***

```python
with open('abc.html','r') as f:
    content = f.read()
#设置html格式参数
part1 = MIMEText(content,'html','utf-8')
```

***添加txt文本格式内容***

```python
#添加一个txt文本附件
with open('abc.txt','r')as h:
    content2 = h.read()
#设置txt参数
part2 = MIMEText(content2,'plain','utf-8')
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
```

***添加照片附件***

```python
#添加照片附件
with open('1.png','rb')as fp:
    picture = MIMEImage(fp.read())
    #与txt文件设置相似
    picture['Content-Type'] = 'application/octet-stream'
    picture['Content-Disposition'] = 'attachment;filename="1.png"'
```

## 2.将内容添加到邮件主体中

```python
message.attach(part1)
message.attach(part2)
message.attach(picture)
```

## 3.登录并发送

```python
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.sina.cn',25)
    smtpObj.login(fromaddr,password)
    smtpObj.sendmail(
        fromaddr,toaddrs,message.as_string())
    print('success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error',e)
```

# 注意事项：

​	一些邮箱登录比如 QQ 邮箱需要 SSL 认证，所以 SMTP 已经不能满足要求，而需要SMTP_SSL，解决办法为：

```python
#启动
smtpObj = smtplib.SMTP()
#连接到服务器
smtpObj.connect(mail_host,25)
#######替换为########
smtpObj = smtplib.SMTP_SSL(mail_host)
```

