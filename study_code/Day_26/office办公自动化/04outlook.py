import win32com
import win32com.client


def makemail(name):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.createItem(0)  # 第一封邮件
    mail.Recipients.Add("%s@microsoft.com" % name)
    mail.Subject = u"尊敬的亲爱的伟大的%s" % name
    mailtext = (u"尊敬的亲爱的伟大的%s" % name)
    mailtext += u"我公司有硅胶娃娃，价格便宜，长的好看，欢迎真人一般的体验"
    mail.Body = mailtext  # 正文
    mail.Send()  # 发送
    outlook.Quit()


names = ["lixin", "shenlingrui", "hefengcheng", "sunyu"]
for name in names:
    makemail(name)
