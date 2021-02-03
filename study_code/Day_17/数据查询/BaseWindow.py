import tkinter


class BaseWindowShow:
    def __init__(self):
        self.win = tkinter.Tk()  # 构造窗体
        self.win.geometry("900x800+0+0")

    def show(self):
        self.win.mainloop()  # 进入消息循环
