import tkinter
from tkinter import ttk


class TableDisplay:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("900x800+0+0")

        self.winTree = ttk.Treeview(self.win, height=800)

        self.winTree["columns"] = ("user", "pwd", "email")
        self.winTree.column("user", width=200)
        self.winTree.column("pwd", width=200)
        self.winTree.column("email", width=200)

        self.winTree.heading("user", text="user")
        self.winTree.heading("pwd", text="password")
        self.winTree.heading("email", text="email")

        self.lineNum = 0

    def addData(self, data):
        dataList = data.split(" # ")
        if len(dataList) == 3:
            self.winTree.insert('', self.lineNum, text=str(self.lineNum),
                                values=(dataList[0], dataList[1], dataList[2]))
            self.lineNum += 1

    def display(self):
        self.winTree.pack()
        self.win.mainloop()
