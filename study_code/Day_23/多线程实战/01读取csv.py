import csv

path = r"D:\code\py\study_code\Day_20\download\华策影视2020.csv"
reader = csv.reader(open(path, 'r'))
for item in reader:
    # print(item)
    for data in item:
        print(data)
