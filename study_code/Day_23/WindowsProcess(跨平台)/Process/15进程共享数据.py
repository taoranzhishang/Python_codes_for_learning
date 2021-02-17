import multiprocessing


def func(num):
    num.value = 10.7  # 修改，没有副本机制


if __name__ == "__main__":
    num = multiprocessing.Value('d', 10.6)  # Value实现数据的共享，还有其它类型，第一个参数指定类型i、d、
    print(num.value, id(num.value), type(num.value))  # 10.6 1886205507984 <class 'float'>
    p = multiprocessing.Process(target=func, args=(num,))
    p.start()
    p.join()
    print(num.value, id(num.value), type(num.value))  # 10.7 1886206715984 <class 'float'>
