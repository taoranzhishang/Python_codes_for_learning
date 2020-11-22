mylist=[[[1,2],[3,4]],
        [[5,6],[7,8]],
        [[9,10],[11,12]]]
print(mylist)#逐层遍历
for idata in mylist:
    #print(idata)
    for jdata in idata:
        #print(jdata)
        for kdata in jdata:
            print(kdata)
print(mylist[0])#第一个元素
print(mylist[0][0])#第一个元素的第一个元素
print(mylist[0][0][0])#第一个元素的第一个元素的第一个元素

for i in range(len(mylist)):
    #print(mylist[i])
    for j in range(len(mylist[i])):
        #print(mylist[i][j])
        for k in range(len(mylist[i][j])):
            print(mylist[i][j][k])