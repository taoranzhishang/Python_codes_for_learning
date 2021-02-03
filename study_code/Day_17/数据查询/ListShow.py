import 数据查询.BaseWindow
import tkinter


class ListShow(数据查询.BaseWindow.BaseWindowShow):
    def __init__(self):
        数据查询.BaseWindow.BaseWindowShow.__init__(self)
        self.mylist = tkinter.Listbox(self.win, width=900, height=800)  # 列表框，继承父类的窗口
        self.mylist.pack()

    def addata(self, insertstr):  # 增加数据
        self.mylist.insert(tkinter.END, insertstr)


'''
mylist=ListShow()
mylist.addata("sadsadsadsa")
mylist.addata("sadsadsadsa")
mylist.addata("sadsadsadsa")
mylist.show()
'''
