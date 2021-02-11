import urllib
import urllib.request
import re


def getPage(url):
    page = urllib.request.urlopen(url).read().decode("utf-8")
    return page


"""
find没有括号抓取全部，有括号，抓取括号内，内容有括号转义字符 \( \)
"""


def getCode(data):
    regexStr = "<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*?)\("
    pat = re.compile(regexStr)
    codeList = pat.findall(data)
    return codeList


url = "http://quote.eastmoney.com/stocklist.html"
data = getPage(url)
print(data)
codeList = getCode(data)
print(codeList)

for code in codeList:
    print(code[0], code[1])
