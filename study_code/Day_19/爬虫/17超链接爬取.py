import urllib
from urllib import request
import re

"""
(http://\s*?)[\"] 提取不带"
http://\s*?[\"] 提取带"
? 非贪婪模式
\"|>|) 3个之一为结束
"""
httpRegex = re.compile(r"(http://\S*?)[\"|>|)]", re.IGNORECASE)

for line in urllib.request.urlopen("http://www.baidu.com"):
    http = httpRegex.findall(line.decode("UTF-8"))
    if http:
        print(http)
