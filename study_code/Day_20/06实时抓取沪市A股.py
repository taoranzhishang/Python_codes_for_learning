import urllib
import urllib.request
import re


# 抓取网页源代码
def getpage(path):
    data = urllib.request.urlopen(path).read().decode("gbk")  # 中文网页
    return data


# 生成网页列表，44个分页
def runpage(min, max):
    for page in range(min, max):
        mystr = "http://quote.stockstar.com/stock/sha_3_1_" + str(page) + ".html"
        print(mystr)


def gettbody(data):
    pat = re.compile("<tbody>[\s\S]*</tbody>")
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
        if newdatalist[i] == "603938":
            myindex = i
    print("myindex", myindex)

    for i in range(myindex, len(newdatalist), 12):
        for j in range(12):
            if i + j < len(newdatalist):
                print(format(newdatalist[i + j], "<15s"), end="  ")
        print("")
    # print(newdatalist)


# runpage(1,45)
# print(getpage("http://quote.stockstar.com/stock/sha_3_1_1.html"))

data = getpage("http://quote.stockstar.com/stock/sha_3_1_1.html")
# print(data)
print(showdata(gettbody(data)))
