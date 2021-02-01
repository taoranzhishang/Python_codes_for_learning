import tkinter
from tkinter import ttk

win = tkinter.Tk()
tree = ttk.Treeview(win)
# self, parent, index, iid=None, **kw
a = tree.insert('', 0, 'a', text='a', values=('1'))  # 父节点（没有则为空），插入的位置（参数相同大的拍前面），自身的id，显示的数据,值
a1 = tree.insert('a', 0, "a1", text="a1", values=('2'))
a2 = tree.insert('a', 1, "a2", text="a2", values='3')
b = tree.insert('', 1, 'b', text='b', values=('4'))
b1 = tree.insert('b', 0, "b1", text="b1", values=('5'))

tree.pack()
win.mainloop()
