# 文件关闭了吗，没有关闭
'''
for line  in open("C:\\Users\\Tsinghua-yincheng\\Desktop\\day16down\\tools\\qqAnd163Password.txt","rb"):
    line=line.decode("gbk","ignore")
    print(line,end="")
'''
# with  open  as file, 自动关闭，
with  open(r"C:\Users\Tsinghua-yincheng\Desktop\day16down\tools\qqAnd163Password.txt", "rb") as file:
    for line in file:
        line = line.decode("gbk", "ignore")
        print(line, end="")
