def func():
    data = ''  # 存储的作用,data始终为空，空变量，没有获取返回值
    r = yield data  # r为a，data为空，返回1个空
    print(1, r, data)
    r = yield data
    print(2, r, data)  # r为b，data为空
    r = yield data
    print(3, r, data)  # 最后一个为空代表结束，不能使用最后一个


coroutine = func()
# print(coroutine.send(None))  # 发送None，表示启动，打印返回的data为空
# print(coroutine.send('a'))  # 打印返回的data为空
# print(coroutine.send('b'))  # 打印返回的data为空
coroutine.send(None)  # 启动，不打印
coroutine.send('a')  # 发送，不打印
