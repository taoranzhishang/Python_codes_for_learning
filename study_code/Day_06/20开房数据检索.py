import codecs

# 路径，读写，汉字编码，忽略错误
file = codecs.open("D:\\Resources\\Python\\Python3开发实践真正完整版 尹成大神主讲 代码 + 课件\
\\day6 Python函数实战\\KaifangX.txt", "rb", "gbk", "ignore")
name = input("input a name:")
while True:
    str = file.readline()  # 读取一行
    if str.find(name) != -1:
        print(str, end="")  # 打印数据
    if str == None:  # 读取失败赋值None
        break
