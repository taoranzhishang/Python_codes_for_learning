'''
读取文本文件
输出首个字符不是'#'的行
'''

file = open("MyText", 'r', encoding="utf-8")  # 以'r'（只读）方式打开.txt文件,编码格式为"utf-8"
counter = 1  # 输出行数

for line in file:  # 遍历文本文件
    if line[0] != '#':  # 取每行的第一个元素，判断首字符不是‘#’则输出该行
        print("第%d行：" % (counter), line)
        counter += 1
    else:  # 占位置用的，以下可以不要
        pass
