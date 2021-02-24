import win32com
import win32com.client


def makeword(name):
    print(name)
    # 操作word,
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Add()  # 插入文档
    word.Visible = True  # 可见

    rng = doc.Range(0, 0)  # 开始位置
    rng.InsertAfter(u"尊敬的%s先生\n" % name)  # 匹配字符串
    rng.InsertAfter(u"    我是高清华，定于2017.10.1与罗玉凤大婚，诚邀来参加婚礼，先准备好分子钱")

    filename = "D:\\code\\py\\study_code\\Day_26\\office办公自动化\\" + name + ".doc"
    doc.SaveAs(filename)  # 保存
    doc.Close(True)  # 关闭

    word.Application.Quit()  # 退出


names = ["李鑫", "申羚锐", "何丰城", "孙雨"]
for name in names:
    makeword(name)
