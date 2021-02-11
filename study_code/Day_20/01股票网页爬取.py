import urllib
import urllib.request


def getPage(url):
    page = urllib.request.urlopen(url).read().decode("utf-8")
    return page


url = "http://quote.eastmoney.com/stocklist.html"
print(getPage(url))
