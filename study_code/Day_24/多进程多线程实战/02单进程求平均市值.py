import csv


def gettotoal(path):
    reader = csv.reader(open(path, "r"))  # 读取
    num = 0
    alldata = 0
    for item in reader:
        if num == 0:
            pass
        else:
            alldata += eval(item[13])  # 累加所有的市值

        num += 1

    return alldata / num


path = r"C:\Users\Tsinghua-yincheng\Desktop\day24\csv\000001.csv"
print(gettotoal(path))
