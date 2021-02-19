import urllib.request
import urllib
import re
import threading
import queue
import time


# http://bbs.tianya.cn/m/post-140-393974-4.shtml
# http://bbs.tianya.cn
# <a class="u-btn pre-btn" href="/m/post-140-393974-4.shtml"></a>

def geteveryurl(data):
    alllist = []
    mylist1 = []
    mylist2 = []

    mylist1 = getallhttp(data)
    if len(mylist1) > 0:
        mylist2 = getabsurl(mylist1[0], data)

    alllist.extend(mylist1)
    alllist.extend(mylist2)
    return alllist


# <a class="u-btn pre-btn" href="/m/post-140-393974-4.shtml"></a>
def getabsurl(url, data):
    try:
        regex = re.compile("href=\"(.*?)\"", re.IGNORECASE)
        httplist = regex.findall(data)
        newhttplist = httplist.copy()  # 深拷贝
        for data in newhttplist:
            if data.find("http://") != -1:
                httplist.remove(data)
            if data.find("javascript") != -1:
                httplist.remove(data)
        hostname = gethostname(url)
        if hostname != None:
            for i in range(len(httplist)):
                httplist[i] = hostname + httplist[i]

        return httplist
    except:
        return []


# http://bbs.tianya.cn/post-140-393974-1.shtml'
# http://bbs.tianya.cn
def gethostname(httpstr):
    try:
        mailregex = re.compile(r"(http://\S*?)/", re.IGNORECASE)
        mylist = mailregex.findall(httpstr)
        if len(mylist) == 0:
            return None
        else:
            return mylist[0]
    except:
        return None


def getallhttp(data):
    try:
        mailregex = re.compile(r"(http://\S*?)[\"|>|)]", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []


def getallemail(data):
    try:
        mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []


def getdata(url):
    try:
        data = urllib.request.urlopen(url).read().decode("utf-8")
        return data  # 没有异常返回字符串
    except:
        return ""  # 发生异常返回空


def BFS(urlstr, myqueue):
    with  sem:  # 锁定数量
        threading.Thread(target=newBFS, args=(urlstr, myqueue)).start()


def newBFS(urlstr, myqueue):  # myqueue 存储邮箱用
    # print(urlstr)
    pagedata = getdata(urlstr)  # 获取网页源代码
    emaillist = getallemail(pagedata)  # 提取邮箱到列表
    if len(emaillist) != 0:  # 邮箱不为空
        for email in emaillist:  # 打印所有邮箱
            print(email)
            myqueue.put(email)  # 队列压入邮箱
    newurllist = geteveryurl(pagedata)  # 抓取所有的url
    if len(newurllist) != 0:  # 判断长度
        for urlstr in newurllist:  # 循环处理每一个url,
            with  sem:  # 锁定数量
                threading.Thread(target=newBFS, args=(urlstr, myqueue)).start()


def BFSget(urlstr, myqueue):
    myqueue.put(urlstr)
    while not myqueue.empty():
        url = myqueue.get()  # 队列弹出的数据
        print(url)  # 打印url链接
        pagedata = getdata(url)  # 获取网页源代码
        emaillist = getallemail(pagedata)  # 提取邮箱到列表
        if len(emaillist) != 0:  # 邮箱不为空
            for email in emaillist:  # 打印所有邮箱
                print(email)
        newurllist = geteveryurl(pagedata)  # 抓取所有的url
        if len(newurllist) != 0:  # 判断长度
            for urlstr in newurllist:  # 循环处理每一个url,
                myqueue.put(urlstr)  # 插入


def saveemail():
    global myqueue
    file = open("email.txt", "wb")
    while True:
        time.sleep(5)
        while not myqueue.empty():
            data = myqueue.get()
            file.write((data + "\r\n").encode("utf-8"))  # 实时写入
            file.flush()

    file.close()


myqueue = queue.Queue(0)
# 定时线程，定时把队列的邮箱写入文件
sem = threading.Semaphore(1000)  # 限制线程的最大数量为10个
timethread = threading.Timer(5, saveemail)  # 延时，5秒以后执行go函数，执行一次，
timethread.start()
# BFS("http://bbs.tianya.cn/m/post-140-393974-5.shtml",myqueue)
BFS(
    "http://www.baidu.com/s?wd=%E5%B2%9B%E5%9B%BD%E5%A4%A7%E7%89%87%20%E7%95%99%E4%B8%8B%E9%82%AE%E7%AE%B1&rsv_spt=1&rsv_iqid=0xc5095fd90001a957&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=43&rsv_sug1=24&rsv_sug7=100&rsv_t=fa71Vz%2Fpl3wbcEm%2FVtCF9XkMoc6Nj9lRZkPphyyIs1I0u%2F4wgFRO7KmJf2EWWaoUzDyY&rsv_sug2=0&inputT=13571&rsv_sug4=14110",
    myqueue)
