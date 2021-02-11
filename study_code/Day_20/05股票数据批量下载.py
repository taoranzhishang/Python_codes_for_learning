import urllib
import urllib.request
import re
import os


def getpage(path):
    data = urllib.request.urlopen(path).read().decode("utf-8")
    return data


# find没有括号抓取全部，有括号，抓取括号内，内容有括号转义字符 \( \)
def getcode(data):
    # regex_str="<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">"
    regex_str = " <li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*?)\("
    pat = re.compile(regex_str)  # 预编译
    codelist = pat.findall(data)
    return codelist


def downloadstock(code, name, date):
    # 文件不存在就创建
    path = "D:\\code\\py\\study_code\\Day_20" + date
    if not os.path.exists(path):
        os.makedirs(path)
    inshorsz = 10
    if code[0:2] == "sh":  # 上海代号是0，深圳代号是1
        inshorsz = 0
    else:
        inshorsz = 1
    if inshorsz != 10:
        url = "http://quotes.money.163.com/service/chddata.html?code=" + str(inshorsz) + \
              code[
              2:] + "&end=20210211&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        path = "D:\\code\\py\\study_code\\Day_20" + date + "\\" + name + ".csv"
        urllib.request.urlretrieve(url, path)  # 根据url下载到路径下


path = "http://quote.eastmoney.com/stocklist.html"
data = getpage(path)  # 抓取了网页源代码
codelist = getcode(data)
# print(codelist)
for code in codelist:
    try:
        downloadstock(code[0], code[1], "20210211")
    except:
        print("error")

# print(code[0],code[1])
