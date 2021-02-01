import tkinter
import os


def search_func():
    str_cmd = entry.get()
    print(str_cmd)
    if str_cmd == "notepad":
        os.system(str_cmd)


win = tkinter.Tk()
win.title("My window")
win.geometry("800x800+300+50")

entry = tkinter.Entry(win,
                      width="30",
                      bg="gray",
                      fg="black")
entry.pack()

button = tkinter.Button(win,
                        text="Search",
                        command=search_func)
button.pack()

win.mainloop()
