import tkinter

win = tkinter.Tk()

label1 = tkinter.Label(win, text="00", bg="red")
label2 = tkinter.Label(win, text="01", bg="blue")
label3 = tkinter.Label(win, text="10", bg="green")
label4 = tkinter.Label(win, text="11", bg="pink")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

win.mainloop()
