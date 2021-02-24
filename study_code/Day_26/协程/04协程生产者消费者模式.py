def creator(cs):
    cs.send(None)  # 启动消费者
    for i in range(1, 100):
        print("生产：", i)
        r = cs.send(i)
        print("消费者返回：", r)
    cs.close()


def consumer():
    r = ''
    while True:
        n = yield r  # 获取生产者发送的数据，n为收到的数据，r为返回的数据，此使为空
        if not n:  # n为空时return
            return
        print("消费：", n)
        r = str(n)


cs = consumer()
ct = creator(cs)
