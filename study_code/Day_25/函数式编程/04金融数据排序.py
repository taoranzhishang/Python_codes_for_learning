import csv
import operator

finance = []
path = r"D:\code\py\study_code\Day_23\多线程实战\csv\000001.csv"
reader = csv.reader(open(path, 'r'))
for item in reader:
    # print(item)
    finance.append(item)

# finance.sort()  # 默认第一个元素排序

finance.sort(key=operator.itemgetter(4))  # 指定索引排序
finance.reverse()  # 反转，从大到小

for line in finance:
    print(line)
