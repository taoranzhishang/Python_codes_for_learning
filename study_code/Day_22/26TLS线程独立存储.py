import threading

data = threading.local()  # 每个线程独立存储空间

t1 = lambda x: x + 1
t2 = lambda x: x + "1"


def printdata(func, x):  # func函数，x代表参数
    data.x = x  # data是一个类，动态绑定，线程独立  =1  =“1”   data.x每个线程中是独立的
    print(id(data.x))  # 不同的地址
    for i in range(5):
        data.x = func(data.x)  # x+1  x+"1"
        print(threading.current_thread().name, data.x)


threading.Thread(target=printdata, args=(t1, 1)).start()
threading.Thread(target=printdata, args=(t2, "1")).start()
