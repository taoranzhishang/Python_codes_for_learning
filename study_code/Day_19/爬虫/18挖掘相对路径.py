import urllib.request
import urllib
import re


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


# print(getdata("http://bbs.tianya.cn/m/post-140-393974-5.shtml"))
# print(getallemail(getdata("http://bbs.tianya.cn/m/post-140-393974-5.shtml")))
# print(getallhttp(getdata("http://bbs.tianya.cn/m/post-140-393974-5.shtml")))

pagedata = getdata("http://bbs.tianya.cn/m/post-140-393974-5.shtml")
print(geteveryurl(pagedata))
print(getallemail(pagedata))

'''
mylist=getallhttp(pagedata)
hostname=gethostname(mylist[0])
print(hostname)
print(getabsurl(mylist[0],pagedata))
'''
