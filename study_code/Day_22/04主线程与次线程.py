import _thread
import win32api


def show(num):
    win32api.MessageBox(0, "你真漂亮", "来自一只舔狗的问候", 0)


"""
主线程结束，次线程就不能发挥作用了，要保证主线程运行
"""
for i in range(5):
    _thread.start_new_thread(show, (i,))

while True:  # 死循环确保主线程运行，卡住主线程（12~16行）
    pass
