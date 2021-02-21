import win32com
import win32com.client

myword = win32com.client.Dispatch("Word.Application")  # 调用系统word功能
path = r"C:\Users\taora\Desktop\中国高校产学研创新基金新一代信息技术创新项目申报指南.docx"  # 处理doc,docx
doc = myword.Documents.Open(path)  # 打开
doc.SaveAs(r"D:\code\py\study_code\Day_25\文件处理\1.txt", 2)  # 编号为2保存为txt ,save必须绝对路径
doc.Close()  # 关闭
myword.Quit()  # 退出
