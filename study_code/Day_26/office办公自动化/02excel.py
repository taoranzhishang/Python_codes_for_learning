import win32com
import win32com.client


def makeexcel(name):
    print(name)
    # 操作word,
    ex = win32com.client.Dispatch("Excel.Application")
    wk = ex.Workbooks.Add()  # 加一张表格
    nowwk = wk.ActiveSheet  # 当前的焦点表格
    ex.Visible = True  # 显示
    for i in range(1, 10):
        nowwk.Cells(i, i).value = name + str(i)  # 插入数据

    filename = "D:\\code\\py\\study_code\\Day_26\\office办公自动化\\" + name + ".xls"
    wk.SaveAs(filename)  # 保存
    wk.Close(True)  # 关闭
    ex.Application.Quit()  # 退出


names = ["李鑫", "申羚锐", "何丰城", "孙雨"]
for name in names:
    makeexcel(name)
