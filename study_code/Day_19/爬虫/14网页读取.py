import urllib
from urllib import request

# webPage=urllib.request.urlopen("http://www.being.com").read()
# print(webPage.decode("UTF-8"))

for line in urllib.request.urlopen("http://www.baidu.com"):
    print(line.decode("UTF-8"))
