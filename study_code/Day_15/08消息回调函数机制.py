import tkinter
import os


def shutdown():
    os.system("shutdown -s -t 60")


win = tkinter.Tk()  # 构造窗体
win.title("My win")  # 窗体标题
win.geometry("800x800+300+0")  # 宽度，高度，x，y
button = tkinter.Button(win, text="有种点我", command=shutdown, width=10, height=5)  # 收到消息执行函数
button2 = tkinter.Button(win, text="我认怂了", command=lambda: os.system("shutdown -a"), width=10, height=8)
button.pack()  # 加载到窗体
button2.pack()
win.mainloop()
