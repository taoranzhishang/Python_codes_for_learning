# 测试后台存在或者不存在

import urllib.request

'''
路径：
单词
webadmin
admin
myadmin
测试.asp  .htm  .html

'''
try:
    data = urllib.request.urlopen("http://www.qinghuabeida.cn/Webadmin").read()
    print(data)
    print("页面存在")
except:
    print("页面不存在")
