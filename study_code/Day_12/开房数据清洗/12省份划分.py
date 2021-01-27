import codecs

"""
读取文件
"""
filepath = r"D:\code\py\study_code\Day_12\开房数据清洗\qDocument_18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")
fileList = file.readlines()
file.close()

"""
按省份清洗
"""
province = [[11, "北京"], [12, "天津"], [13, "河北"], [14, "山西"], [15, "内蒙古"], [21, "辽宁"], [22, "吉林"], [23, "黑龙江"],
            [31, "上海"], [32, "江苏"], [33, "浙江"], [34, "安徽"], [35, "福建"], [36, "江西"], [37, "山东"], [41, "河南"],
            [42, "湖北"], [43, "湖南"], [44, "广东"], [45, "广西"], [46, "海南"], [50, "重庆"], [51, "四川"], [52, "贵州"],
            [53, "云南"], [54, "西藏"], [61, "陕西"], [62, "甘肃"], [63, "青海"], [64, "宁夏"], [65, "新疆"], [71, "台湾"],
            [81, "香港"], [82, "澳门"]]
provinceFileList = []
length = len(province)
for data in province:
    provinceFilepath = "D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\省份\\" + data[1] + ".txt"
    infoDoc = open(provinceFilepath, "wb")
    provinceFileList.append(infoDoc)  # 文件列表

for data in fileList:
    lineList = data.split(',')
    provinceCode = lineList[1][0:2]
    for i in range(length):
        if str(province[i][0]) == provinceCode:
            provinceFileList[i].write(data.encode("utf-8"))
            break

for file in provinceFileList:
    file.close()
