import smtplib  # 发邮件
from email.mime.text import MIMEText  # 邮件文本

isOK = False
password = "tsinghua88480"  # 密码

try:
    SMTPsever = "smtp.163.com"  # 服务器
    Sender = "yincheng8848@163.com"  # 发送邮件的地址

    Message = "Hello  Python  Hello Baby,你好，小伙子，过来跟哥学python吧，"  # 发送的内容
    msg = MIMEText(Message)  # 转化邮件文本

    msg["Subject"] = "你好小伙子，好久不见别来无恙乎"  # 邮件标题
    msg["From"] = Sender  # 邮件发送者
    msg["To"] = "yincheng8848@163.com"  # 谁来收

    mailsever = smtplib.SMTP(SMTPsever, 25)  # 邮件服务器25端口
    mailsever.login(Sender, password)  # 登陆
    mailsever.sendmail(Sender,
                       ["13001087800@163.com", "yincheng8848@163.com"],
                       msg.as_string())
    mailsever.quit()
    isOK = True
except smtplib.SMTPAuthenticationError:
    isOK = False

if isOK:
    print(password, "right")
else:
    print(password, "wrong")
