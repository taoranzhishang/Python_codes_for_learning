import tkinter
import tkinter.ttk


class TreeWindow:
    def __init__(self):
        self.win = tkinter.Tk()
        self.tree = tkinter.ttk.Treeview(self.win)  # 树状
        self.ysb = tkinter.ttk.Scrollbar(self.win, orient="vertical", command=self.tree.yview())  # y轴滚动
        self.xsb = tkinter.ttk.Scrollbar(self.win, orient="horizontal", command=self.tree.xview())  # x轴滚动
        self.tree.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
        self.tree.grid(row=0, column=0)
        self.ysb.grid(row=0, column=1)
        self.xsb.grid(row=1, column=0)
        self.win.grid()  # 表格展示

    def display(self):
        self.win.mainloop()


win=TreeWindow()
win.display()