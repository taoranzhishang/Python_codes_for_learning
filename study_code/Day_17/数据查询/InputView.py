import tkinter
from tkinter import ttk
import 数据查询.BigdataFind


class InputView:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("800x600+300+0")  # 800宽度，800高度，x,y坐标，左上角

        self.entry = tkinter.Entry(self.win)  # input
        self.entry.place(x=0, y=0)
        self.button = tkinter.Button(self.win, text="搜索", command=self.search)
        self.button.place(x=200, y=0)

        self.comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        self.comboxlist = ttk.Combobox(self.win, textvariable=self.comvalue, width=80)  # 初始化

        self.comboxlist["values"] = ("listshow", "textshow", "tableshow")
        self.comboxlist.current(0)  # 选择第一个
        self.comboxlist.bind("<<ComboboxSelected>>", self.go)  # 绑定事件
        self.comboxlist.place(x=0, y=50)
        self.howtoshow = "listshow"

        self.comvaluefile = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        self.comboxlistfile = ttk.Combobox(self.win, textvariable=self.comvaluefile, width=80)  # 初始化
        self.comboxlistfile["values"] = (r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\csdn.txt",
                                         r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\kaifangX.txt",
                                         r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\QQ.txt")
        self.comboxlistfile.current(0)  # 选择第一个
        self.comboxlistfile.bind("<<ComboboxSelected>>", self.filego)  # 绑定事件
        self.comboxlistfile.place(x=0, y=100)
        self.howtoshowfile = r"Z:\F\第一阶段视频\20170424\vedio\大数据相关数据\csdn.txt"

        pass

    def go(self, *args):
        self.howtoshow = self.comboxlist.get()  # 保存选中的值
        print(self.comboxlist.get())  # 选中当前的值

    def filego(self, *args):
        self.howtoshowfile = self.comboxlistfile.get()  # 保存选中的值
        print(self.comboxlistfile.get())  # 选中当前的值

    def show(self):
        self.win.mainloop()

    def search(self):
        print("start search", self.entry.get())
        big = 数据查询.BigdataFind.bigdatafind(self.howtoshowfile, self.howtoshow)
        big.find(self.entry.get())
        big.show()
