import tkinter


def call(event):
    print(event.x, event.y)


win = tkinter.Tk()
frame = tkinter.Frame(win, width=200, height=200)
frame.bind("<Motion>", call)  # 监控当前窗口内下，鼠标位置

frame.pack()
win.mainloop()
