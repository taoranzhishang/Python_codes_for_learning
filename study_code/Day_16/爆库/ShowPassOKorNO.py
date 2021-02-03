import tkinter
import 爆库.MySQLTest


class Listshowdata:
    def __init__(self, ip, user):
        self.win = tkinter.Tk()  # 构造窗体
        self.win.geometry("900x800+0+0")
        self.mylist = tkinter.Listbox(self.win, width=900, height=800)  # 列表框

        self.crack = 爆库.MySQLTest.MySQLCrack(ip, user)
        self.button = tkinter.Button(self.win, text="破解", command=self.startgo)
        self.button.pack()
        self.mylist.pack()

    def startgo(self):
        self.crack.startcrack(self)  # 传递自身这个对象地址

    def addata(self, insertstr):  # 增加数据

        self.mylist.insert(tkinter.END, insertstr)
        # 256,text,文本，

    def show(self):
        self.win.mainloop()  # 进入消息循环
