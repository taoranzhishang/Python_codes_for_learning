import codecs

"""
读取文件
"""
filepath = r"D:\code\py\study_code\Day_12\开房数据清洗\qDocument_18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")
fileList = file.readlines()
file.close()

"""
按出生年份清洗
"""
year = [x for x in range(1900, 2021)]
yearFileList = []
length = len(year)
for data in year:
    yearFilepath = "D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\年份\\" + str(data) + ".txt"
    infoDoc = open(yearFilepath, "wb")
    yearFileList.append(infoDoc)  # 文件列表

for data in fileList:
    lineList = data.split(',')
    yearInfo = lineList[1][6:10]
    for i in range(length):
        if str(year[i]) == yearInfo:
            yearFileList[i].write(data.encode("utf-8"))
            break

for file in yearFileList:
    file.close()
