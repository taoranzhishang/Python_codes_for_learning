import threading
import _thread
import win32api

"""
1、基于函数创建，遍历调用函数，不考虑冲突、通信时使用
2、基于类的继承创建，遍历实例化，使用较多
3、基于threading类的构造函数实现多线程
多线程是几个同时执行，顺序不一，乱序
"""

"""
基于函数
"""
# def show(num):
#     win32api.MessageBox(0, "你真漂亮" + str(num), "来自一只舔狗的问候", 1)

"""
顺序执行，逐个执行
"""
# for i in range(5):
#     show()

"""
多线程，多个同时执行
"""
# for i in range(5):
#     _thread.start_new_thread(show, (i,))  # ()元组用于传递参数
# show(5)
#-------------------------------------------------------------
"""
基于类的继承
"""
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         threading.Thread.__init__(self)  # 父类初始化
#         self.num = num
#
#     def run(self):  # 重写
#         win32api.MessageBox(0, "Your are so beautiful" + str(self.num), "From a single dog", 0)
#
#
# for i in range(5):
#     t = MyThread(i)  # 实例化
#     t.start()  # 开启
#
# while True:
#     pass

#-------------------------------------------------------------------------------
"""
基于threading.Thread类的构造函数实现多线程
"""
# def show(num):
#     win32api.MessageBox(0, "你真漂亮" + str(num), "来自一只舔狗的问候", 1)
"""
target:目标函数，args:参数且为元组
"""
# threading.Thread(target=show, args=(1,)).start()
# threading.Thread(target=show, args=(2,)).start()
# threading.Thread(target=show, args=(3,)).start()
