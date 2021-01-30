import tkinter

win = tkinter.Tk()
win.title("Display")
win.geometry("800x700+300+100")
displayList = tkinter.Listbox(win, width=100)  # 列表框

for item in ["Hello world", "你好世界", "Hello China", "你好天朝"]:  # 内容插入
    displayList.insert(tkinter.END, item)  # 尾部插入

displayList.pack()

win.mainloop()
