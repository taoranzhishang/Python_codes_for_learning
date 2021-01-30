import tkinter

win = tkinter.Tk()
win.title("My window")
win.geometry("800x800+300+40")
# entry = tkinter.Entry(win,
#                       width=50,
#                       bg="gray",
#                       fg="red")
entry = tkinter.Entry(win,  # 父窗体
                      show='*',  # 输入内容展示为指定字符
                      width=50,  # 宽度
                      bg="gray",  # 输入框背景色
                      fg="red")  # 字体颜色
entry.pack()  # 加载
win.mainloop()
