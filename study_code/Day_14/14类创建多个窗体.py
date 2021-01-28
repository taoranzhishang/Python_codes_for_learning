import tkinter

"""
多窗体实战
"""


class MyWindow:
    def __init__(self, winTitle, width, height, x, y):
        """
        注意self的使用
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        winParameters = "%dx%d+%d+%d" % (self.width, self.height, self.x, self.y)
        self.myWin = tkinter.Tk()
        self.myWin.title(winTitle)
        self.myWin.geometry(winParameters)

    def display(self):
        self.myWin.mainloop()


"""
参数实在实例化对象时传入的
功能要调用函数才能实现
"""
win1 = MyWindow("win1", 400, 500, 300, 300)
win1.display()
win2 = MyWindow("win2", 800, 800, 500, 300)
win2.display()
