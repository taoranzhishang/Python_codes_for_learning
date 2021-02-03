import tkinter
from tkinter import ttk
import 爆库.ShowPassOKorNO


class InputView:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("800x600+300+0")  # 800宽度，800高度，x,y坐标，左上角

        self.label1 = tkinter.Label(self.win, text="ip")
        self.label2 = tkinter.Label(self.win, text="user")
        self.label1.place(x=0, y=0)
        self.label2.place(x=0, y=100)

        self.entry1 = tkinter.Entry(self.win)  # input
        self.entry1.place(x=100, y=0)

        self.entry2 = tkinter.Entry(self.win)  # input
        self.entry2.place(x=100, y=100)

        self.button = tkinter.Button(self.win, text="破解", command=self.search)
        self.button.place(x=100, y=200)

    def show(self):
        self.win.mainloop()

    def search(self):
        mylist = 爆库.ShowPassOKorNO.Listshowdata(self.entry1.get(), self.entry2.get())
        mylist.show()


inputs = InputView()
inputs.show()
