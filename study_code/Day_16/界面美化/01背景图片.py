import tkinter

"""
只能使用gif
"""
win = tkinter.Tk()
winPhoto = tkinter.PhotoImage(file=r"D:\code\py\study_code\Day_16\界面美化\bg.gif")
winLabel = tkinter.Label(win, image=winPhoto)
winLabel.pack()
win.mainloop()
