import urllib
from urllib import request
import re

mailRegex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)

webPage = urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml").read()
mail = mailRegex.findall(webPage.decode("UTF-8"))
print(mail)

# for line in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
#     # print(line.decode("UTF-8"))
#     mail = mailRegex.findall(line.decode("utf-8"))
#     if mail:
#         print(mail)
