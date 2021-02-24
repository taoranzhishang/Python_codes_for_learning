import win32com
import win32com.client


def makeppt(name):
    try:
        ppt = win32com.client.Dispatch("PowerPoint.Application")
        pres = ppt.Presentations.Add()  # 增加一个页面
        ppt.Visible = True

        s1 = pres.Slides.Add(1, 1)  # 增加一个页面
        s1_0 = s1.Shapes[0].TextFrame.TextRange  # 找到第一个文本
        s1_0.Text = "尊敬的%s" % name

        s1_1 = s1.Shapes[1].TextFrame.TextRange  # 找到第2个文本
        s1_1.Text = "hello world"

        filename = "D:\\code\\py\\study_code\\Day_26\\office办公自动化\\" + name + ".ppt"
        pres.SaveAs(filename)  # 保存
        pres.Close()  # 关闭
        ppt.Application.Quit()  # 退出
    except AttributeError:
        pass


names = ["李鑫", "申羚锐", "何丰城", "孙雨"]
for name in names:
    makeppt(name)
