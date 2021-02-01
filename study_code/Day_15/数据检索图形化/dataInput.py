import tkinter
import dataSearch


class InputView:
    def __init__(self):
        """
        初始化窗口、控件参数
        """
        self.win = tkinter.Tk()
        self.win.geometry("400x400+300+0")

        self.entry = tkinter.Entry(self.win)
        self.entry.place(x=0, y=0)

        self.button = tkinter.Button(self.win, text="Search", command=self.launcher)
        self.button.place(x=200, y=0)

    def display(self):
        """
        展示窗口函数
        """
        self.win.mainloop()

    def launcher(self):
        """
        检索启动函数
        """
        print("Start search", self.entry.get())
        searching = dataSearch.DataSearch(r"D:\code\py\study_code\Day_12\开房数据清洗\省份\四川.txt")
        searching.search(self.entry.get())  # 搜索输入的内容
        searching.display()
