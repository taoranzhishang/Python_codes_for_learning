import os
path=r"C:\Users\Tsinghua-yincheng\Desktop\day19"
mystack=[]
mystack.append([path,0])

while  len(mystack)!=0:
    pathlist=mystack.pop()#取出路径与层次
    filelist=os.listdir(pathlist[0]) #遍历路径

    num=pathlist[1]#代表层次
    headstr=""
    for  i  in range(num): #控制层次感
        headstr+="      "

    #for filename in filelist:
    for i in range(len(filelist)):
        filename=filelist[len(filelist)-1-i]
        filepath = os.path.join(pathlist[0], filename)  # 链接，取得绝对路径
        if os.path.isdir(filepath):#文件夹
            print(headstr,"文件夹", filepath)
            mystack.append([filepath,num+1])
        else:#文件
            print(headstr,"文件",filepath)

