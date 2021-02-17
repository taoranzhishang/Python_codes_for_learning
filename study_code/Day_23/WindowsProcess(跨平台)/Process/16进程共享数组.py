import multiprocessing


def func(arr):
    for i in range(4):
        arr[i] = 0  # 修改，没有副本机制


if __name__ == "__main__":
    arr = multiprocessing.Array('i', [1, 2, 3, 4])  # Array实现数组的共享，还有其它类型，第一个参数指定类型i int类型
    print(arr[:], id(arr),
          type(arr))  # [1, 2, 3, 4] 2132119530752 <class 'multiprocessing.sharedctypes.SynchronizedArray'>
    p = multiprocessing.Process(target=func, args=(arr,))
    p.start()
    p.join()
    print(arr[:], id(arr),
          type(arr))  # [0, 0, 0, 0] 2132119530752 <class 'multiprocessing.sharedctypes.SynchronizedArray'>
