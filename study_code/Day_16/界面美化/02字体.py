import tkinter

win = tkinter.Tk()
label = tkinter.Label(win,
                      text="Hello World\n你好世界",
                      font=("华文楷体", 40),
                      bg="pink",
                      fg="blue",
                      width=100,
                      height=100)
label.pack()
win.mainloop()
