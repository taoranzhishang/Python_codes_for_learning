import tkinter


def call(event):
    print(event.keysym)


win = tkinter.Tk()
frame = tkinter.Frame(win, width=200, height=200)  # 限定范围
frame.bind("<Key>", call)  # 事件绑定，激发函数
frame.focus_set()  # 获取焦点
frame.pack()

win.mainloop()
