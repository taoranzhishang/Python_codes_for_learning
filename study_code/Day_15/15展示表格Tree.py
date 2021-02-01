import tkinter
from tkinter import ttk

win = tkinter.Tk()

tree = ttk.Treeview(win)  # 显示表格或树

tree["columns"] = ("Name", "Age", "Height")
tree.column("Name", width=100)  # 表示列，不显示
tree.column("Age", width=100)
tree.column("Height", width=100)

tree.heading("Name", text="姓名")  # 表头
tree.heading("Age", text="年龄")
tree.heading("Height", text="身高")

tree.insert('', 0, text="line1", values=('1', '2', '3'))  # 插入行
tree.insert('', 1, text="line2", values=('1', '2', '3'))
tree.insert('', 2, text="line3", values=('1', '2', '3'))
tree.insert('', 3, text="line4", values=('1', '2', '3'))

tree.pack()
win.mainloop()
