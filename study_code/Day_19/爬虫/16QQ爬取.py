import urllib
from urllib import request
import re

QQRegex = re.compile("[1-9]\d{4,10}", re.IGNORECASE)

for line in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
    line = line.decode("UTF-8")
    if line.find("QQ") != -1 or line.find("qq") != -1 or line.find("Qq") != -1:
        QQ = QQRegex.findall(line)
        if QQ:
            print(QQ)
