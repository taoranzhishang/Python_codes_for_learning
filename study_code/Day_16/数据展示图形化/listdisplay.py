import tkinter


class ListDisplay:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("900x800+0+0")

        self.winList = tkinter.Listbox(self.win, width=900, height=800)
        self.winList.pack()

    def addData(self, data):
        self.winList.insert(tkinter.END, data)

    def display(self):
        self.win.mainloop()
