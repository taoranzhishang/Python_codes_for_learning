import tkinter
from tkinter import ttk


def run(*args):  # 处理事件
    print(comList.get())


win = tkinter.Tk()
win.title("My window")
win.geometry("800x500+300+200")

comValue = tkinter.StringVar()  # 用窗体自带文本，新建一个值
comList = ttk.Combobox(win, textvariable=comValue)  # 初始化comList的内容
comList["values"] = (1, 2, 3, 4)  # 填充值,元素、列表可行
comList.current(0)  # 选择第1个，展示第1个，不使用不选择，下拉选择框为空
comList.bind("<<ComboboxSelected>>", run)  # 绑定事件
comList.pack()
win.mainloop()
