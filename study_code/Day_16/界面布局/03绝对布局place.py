import tkinter

win = tkinter.Tk()
label1 = tkinter.Label(win, text="陶然至上", bg="blue")
label2 = tkinter.Label(win, text="Colder", bg="pink")
label3 = tkinter.Label(win, text="sb", bg="gray")

"""
绝对布局，不随窗体大小改变大小位置
"""
# label1.place(x=0,y=0)
# label2.place(x=50,y=50)
# label3.place(x=100,y=100)
"""
输入s，远离窗体s边界
输入n，远离窗体n边界
输入sw，远离窗体sw边界
"""
label1.place(x=0, y=0, anchor='s')
label2.place(x=50, y=50, anchor='n')
label3.place(x=100, y=100, anchor="sw")

win.mainloop()
