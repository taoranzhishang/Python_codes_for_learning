import tkinter

win = tkinter.Tk()
"""
fill扩张，X，Y,BOTH同步变化，side贴边，LEFT靠左,RIGHT靠右，TOP靠上，BOTTOM靠下，默认TOP
靠左、右时，Label宽度固定，X方向被限制同步；靠上、下时Label高度固定，Y方向不同步
靠哪个方向，哪个方向不变
"""
# label1=tkinter.Label(win,text="label1",bg="blue")
# label2=tkinter.Label(win,text="label2",bg="pink")

# label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
# label2.pack(fill=tkinter.BOTH,side=tkinter.RIGHT)

# button=tkinter.Button(win,text="button")
# button.pack(fill=tkinter.Y,side=tkinter.LEFT)

listBox = tkinter.Listbox(win)
listBox.pack(fill=tkinter.BOTH, side=tkinter.BOTTOM)

win.mainloop()
