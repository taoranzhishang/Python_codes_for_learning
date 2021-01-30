import tkinter

win = tkinter.Tk()
win.title("My window")
win.geometry("800x800+300+0")  # 设置位置和大小
button = tkinter.Button(win,
                        text="button",  # 名称
                        width=8,  # 宽度
                        height=4,  # 高度
                        command=lambda: print("Hello World"),  # 执行
                        bg="green",  # 按钮背景色
                        fg="pink")  # 字体颜色
button.pack()  # 加载到窗体
label = tkinter.Label(win, text="label")  # 标签，显示文本
label.pack()  # 加载到标签
newLabel = tkinter.Label(win,  # 父窗体
                         anchor=tkinter.CENTER,  # 位置S,N,SW,SE...
                         text="NewLabel",  #
                         bg="blue",  # 背景颜色
                         fg="red",  # 标签颜色
                         width=100,  # 宽度
                         height=50)  # 高度
newLabel.pack()  # 加载到标签

win.mainloop()
