import tkinter


class DataDisplay:
    def __init__(self):
        """
        初始化窗口、控件、参数
        """
        self.win = tkinter.Tk()
        self.win.geometry("900x800+0+0")
        self.dataList = tkinter.Listbox(self.win, width=900, height=800)
        self.dataList.pack()

    def display(self):
        self.win.mainloop()

    def addData(self, data):
        """
        插入数据函数
        """
        self.dataList.insert(tkinter.END, data)
