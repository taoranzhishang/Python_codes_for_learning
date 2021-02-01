import tkinter

win = tkinter.Tk()
win.title("My window")
win.geometry("800x800+300+50")

editor = tkinter.Text(win)
editor.insert(tkinter.INSERT, "12345\r\n")
editor.insert(tkinter.INSERT, "一二三四五\r\n")
editor.pack()

win.mainloop()
