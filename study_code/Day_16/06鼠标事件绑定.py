import tkinter


def tell(event):
    print(event.x, event.y)


win = tkinter.Tk()

frame = tkinter.Frame(win, width=200, height=200)  # 创建框架，限定范围，范围内才生效
frame.bind("<Button-1>", tell)  # 激发的函数,<Button-1>左键，<Button-3>右键
frame.pack()

label = tkinter.Label(frame, width=10, height=10, bg="pink")
label.pack()

win.mainloop()
