import urllib
import urllib.request

for i in range(100, 150):
    url = "http://hq.sinajs.cn/list=sz300" + str(i)
    print(urllib.request.urlopen(url).read().decode("gbk"))

'''
path="C:\\Users\\Tsinghua-yincheng\\Desktop\\day25\\down"
for  i  in range(100,150):
    url="http://image.sinajs.cn/newchart/daily/n/sz300"+str(i)+".gif"
    urllib.request.urlretrieve(url,path+"\\"+str(i)+".gif")
'''
