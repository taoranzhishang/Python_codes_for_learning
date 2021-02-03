import tkinter
import 数据查询.BaseWindow


class Textshow(数据查询.BaseWindow.BaseWindowShow):
    def __init__(self):
        数据查询.BaseWindow.BaseWindowShow.__init__(self)
        self.text = tkinter.Text(self.win, width=900, height=800)  # 文本编辑器，继承父类的窗口
        self.text.pack()

    def addata(self, insertstr):  # 增加数据
        self.text.insert(tkinter.INSERT, insertstr)


'''
mylist=Textshow()
mylist.addata("sadsadsadsa\r\n")
mylist.addata("sadsadsadsa\r\n")
mylist.addata("sadsadsadsa")
mylist.show()
'''
