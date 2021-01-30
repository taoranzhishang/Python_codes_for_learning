import smtplib  # 发邮件
from email.mime.text import MIMEText  # 邮件文本


class SendMail:
    def __init__(self, SMTPsever, Sender, password):
        self.SMTPsever = "smtp.163.com"  # 服务器
        self.Sender = "yincheng8848@163.com"  # 发送邮件的地址
        self.password = "tsinghua8848"  # 密码
        self.mailsever = smtplib.SMTP(self.SMTPsever, 25)  # 邮件服务器25端口
        self.mailsever.login(self.Sender, self.password)  # 登陆

    def Send(self, Message, title, maillist):
        msg = MIMEText(Message)  # 转化邮件文本
        msg["Subject"] = title  # 邮件标题
        msg["From"] = self.Sender  # 邮件发送者
        msg["To"] = "yincheng8848@163.com"  # 谁来收

        self.mailsever.sendmail(self.Sender,
                                maillist,
                                msg.as_string())

    def exit(self):
        self.mailsever.quit()


sender1 = SendMail("smtp.163.com", "yincheng8848@163.com", "tsinghua8848")
sender1.Send("你好你借我的钱啥时候还 ", "再不还我要吃不上饭", ["13001087800@163.com", "yincheng8848@163.com"])
sender1.exit()
