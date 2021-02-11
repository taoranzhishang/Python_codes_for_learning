import urllib
import urllib.request
import random
import re

user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']


# 抓取网页源代码
def getpage(path):
    # 冒充其他浏览器
    request = urllib.request.Request(url=path, headers={"User-Agent": random.choice(user_agent)})
    response = urllib.request.urlopen(request)  # 会话，打开网页
    data = response.read().decode("gbk")  # 读取网页并且编码
    return data


# 生成网页列表，44个分页
def runpage(min, max):
    for page in range(min, max):
        mystr = "http://quote.stockstar.com/fund/stock_3_1_" + str(page) + ".html"
        print(mystr)

        data = getpage(mystr)  # 抓取每一个页面
        # print("data",data)
        showdata(gettbody(data))  # 显示数据


def gettbody(data):
    pat = re.compile("<tbody class=\"tbody_right\" id=\"datalist\">[\s\S]*</tbody>")
    body = pat.findall(data)  # 提取body的所有数据

    patnew = re.compile(">(.*?)<")  # 提取表格内部数据
    datalist = patnew.findall(body[0])  # 第一个
    return datalist


def showdata(datalist):
    newdatalist = datalist.copy()  # 深拷贝
    for data in datalist:
        if data == "":
            newdatalist.remove(data)  # 删除空格

    myindex = -1
    for i in range(len(newdatalist)):
        newdatalist[i].strip()  # 删除前后空格
        if newdatalist[i] == "市盈率":
            myindex = i + 1

    if myindex == -1:
        myindex == 0
    for i in range(myindex, len(newdatalist), 10):
        for j in range(10):
            if i + j < len(newdatalist):
                print(format(newdatalist[i + j], "<15s"), end="  ")
        print("")
    # print(newdatalist)


# runpage(1,45)
# print(getpage("http://quote.stockstar.com/stock/sha_3_1_1.html"))

# data =getpage("http://quote.stockstar.com/stock/sha_3_1_1.html")

runpage(1, 27)
