import urllib
import urllib.request
import threading
import time

"""
一个行业一个进程
一个公司一个线程
"""


def getstock(i):
    url = "http://hq.sinajs.cn/list=sz300" + str(i)
    print(urllib.request.urlopen(url).read().decode("gbk"))


while True:
    time.sleep(1)
    threadlist = []
    for i in range(100, 150):
        th = threading.Thread(target=getstock, args=(i,))
        th.start()
        threadlist.append(th)

    for th in threadlist:
        th.join()
    print("抓取完成")
