import tkinter


class TextDisplay:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("900x800+0+0")

        self.winText = tkinter.Text(self.win)
        self.winText.pack()

    def addData(self, data):
        self.winText.insert(tkinter.INSERT, data)

    def display(self):
        self.win.mainloop()
