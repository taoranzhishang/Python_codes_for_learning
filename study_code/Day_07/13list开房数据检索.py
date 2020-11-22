import codecs  # 编码

file = codecs.open("D:\\Resources\\Python\\Python3开发实践真正完整版 尹成大神主讲 代码 + 课件\
\\day6 Python函数实战\\KaifangX.txt", "rb", "gbk", "ignore")

listName = file.readlines()  # 多行读取，返回list
print(type(listName))

while True:
    name = input("请输入要搜索的负心人：")
    data = 0
    for line in listName:
        if line.find(name) != -1:  # 挨个搜索
            print(line)
            data += 1
    print("总共%d条" % data)
