mydict={"abcd":10,"12345":12345}

print(mydict)

password="a1bcd"
times=100
if password in mydict:
    mydict[password]+=times#存在就叠加，更新
else:
    mydict[password]=times#不存在就新建

print(mydict)