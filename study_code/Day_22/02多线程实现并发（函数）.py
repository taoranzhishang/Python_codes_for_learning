import win32api  # 引用系统函数
import _thread  # 多线程

"""
基于函数实现多线程，_thread.start_new_thread(show, (i,))，遍历调用函数
"""


def show(num):
    win32api.MessageBox(0, "你真漂亮", "来自一只舔狗的问候", 1)


"""
顺序执行，逐个执行
"""
# for i in range(5):
#     show()

"""
多线程，多个同时执行
"""
for i in range(5):
    _thread.start_new_thread(show, (i,))  # ()元组用于传递参数
show(5)
