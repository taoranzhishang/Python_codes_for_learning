import _thread

num = 0


def add():
    global num
    for i in range(1000000):
        num += 1
    print(num)


# for i in range(5):
#     add()

"""
线程冲突：一个资源同时被多个调用会出错
"""
for i in range(5):
    _thread.start_new_thread(add, ())

while True:
    pass
