import codecs
import pickle

filepath = r"D:\code\py\study_code\Day_12\开房数据清洗\qDocument_18.txt"
file = codecs.open(filepath, "rb", "utf-8", "ignore")  # 按照指定编码
myList = file.readlines()  # 返回一个list,读取到内存
file.close()
print("load")

areaList = []
files = open("sfz.bin", "rb")
areaList = pickle.load(files)  # 对象的文件加载到内存
files.close()
areaFileList = []  # 装下所有文件对象
length = len(areaList)  # 长度

for data in areaList:
    kfFilepath = "D:\\code\\py\\study_code\\Day_12\\开房数据清洗\\area\\" + data[1] + ".txt"
    kfFile = open(kfFilepath, "wb")
    areaFileList.append(kfFile)

print("create")

for line in myList:
    lineList = line.split(",")  # 字符串切割
    areaCode = lineList[1][0:6]  # 取出6个字符
    for i in range(length):
        if str(areaList[i][0]) == areaCode:  # 对比是哪个文件
            areaFileList[i].write(line.encode("utf-8"))
            break

print("over")
for kfFile in areaFileList:  # 关闭文件
    kfFile.close()
