import tkinter
import tkinter.ttk
import os


class TreeWindow:
    def __init__(self, filepath):
        self.win = tkinter.Tk()
        self.tree = tkinter.ttk.Treeview(self.win)  # 树状
        self.ysb = tkinter.ttk.Scrollbar(self.win, orient="vertical", command=self.tree.yview())  # y轴滚动条
        self.xsb = tkinter.ttk.Scrollbar(self.win, orient="horizontal", command=self.tree.xview())  # x轴滚动条
        self.tree.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)

        self.tree.heading("#0", text="Path", anchor='w')  # 初始化表头，w 靠近西方
        self.e = tkinter.StringVar()
        self.e.set("请选择文件")
        self.entry = tkinter.Entry(self.win, textvariable=self.e)
        self.tree.bind("<<TreeviewSelect>>", self.select)

        self.win.grid()  # 表格展示
        self.tree.grid(row=0, column=0)
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.entry.grid(row=0, column=2)

        self.filepath = filepath
        root = self.tree.insert('', "end", text=self.filepath, open=True)
        self.loadTree(root, self.filepath)

    def loadTree(self, parent, rootPath):
        for path in os.listdir(rootPath):  # 遍历当前目录全部文件
            absPath = os.path.join(rootPath, path)  # 路径拼接
            oid = self.tree.insert(parent, "end", text=path, open=False)  # 插入树枝
            if os.path.isdir(absPath):
                print("文件夹", path)
                self.loadTree(oid, absPath)
            else:
                print("文件", path)

    def select(self, event):
        self.select = event.widget.selection()
        for idx in self.select:
            print(self.tree.item(idx)["text"])
            self.e.set(self.tree.item(idx)["text"])

    def display(self):
        self.win.mainloop()


fileTree = TreeWindow(r"D:\code\py\study_code\Day_16")
fileTree.display()
