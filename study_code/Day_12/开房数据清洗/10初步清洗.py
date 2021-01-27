import codecs

"""
读取文件
"""
filepath = r"D:\Resources\Python\Python3开发实践真正完整版 尹成大神主讲 代码 + 课件\day6 Python函数实战\kaifangX.txt"
file = codecs.open(filepath, "rb", "gbk", "ignore")
fileList = file.readlines()
file.close()
"""
数据清洗
"""
qFilepath = r"D:\code\py\study_code\Day_12\开房数据清洗\qDocument_18.txt"
uFilepath = r"D:\code\py\study_code\Day_12\开房数据清洗\uDocument.txt"
qDocument = open(qFilepath, "wb")
uDocument = open(uFilepath, "wb")

for data in fileList:
    lineList = data.split(',')
    if len(lineList) >= 2:
        if len(lineList[1]) == 18:
            qDocument.write(data.encode("utf-8"))
        else:
            uDocument.write(data.encode("utf-8"))

qDocument.close()
uDocument.close()
