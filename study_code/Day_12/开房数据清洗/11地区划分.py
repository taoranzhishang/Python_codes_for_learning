import codecs

"""
读取文件
"""
filepath = r"D:\code\py\study_code\Day_12\开房数据清洗\qDocument_18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")
fileList = file.readlines()
file.close()

"""
按地区清洗
"""
area = [[1, "华北"], [2, "东北"], [3, "华东"], [4, "中南"], [5, "西南"], [6, "西北"]]
areaFileList = []
length = len(area)
for data in area:
    areaFilepath = "D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\" + data[1] + ".txt"
    infoDoc = open(areaFilepath, "wb")
    # print(infoDoc)
    # < _io.BufferedWriter
    # name = 'D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\华北.txt' >
    # < _io.BufferedWriter
    # name = 'D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\东北.txt' >
    # < _io.BufferedWriter
    # name = 'D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\华东.txt' >
    # < _io.BufferedWriter
    # name = 'D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\中南.txt' >
    # < _io.BufferedWriter
    # name = 'D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\西南.txt' >
    # < _io.BufferedWriter
    # name = 'D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\地区\\西北.txt' >
    areaFileList.append(infoDoc)  # 文件列表

for data in fileList:
    lineList = data.split(',')
    areaCode = lineList[1][0]
    for i in range(length):
        if str(area[i][0]) == areaCode:
            areaFileList[i].write(data.encode("utf-8"))
            break

for file in areaFileList:
    file.close()
