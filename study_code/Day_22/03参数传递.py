import _thread
import win32api


def show(num):
    win32api.MessageBox(0, "你真漂亮", "来自一只舔狗的问候", 0)


"""
传递参数
"""
for i in range(5):
    _thread.start_new_thread(show, (i,))
show(10)
