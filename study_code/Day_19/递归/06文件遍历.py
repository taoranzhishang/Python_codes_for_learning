import os

fileList = os.listdir(r"/study_code/Day_19")
for file in fileList:
    if os.path.isdir("D:\\code\\py\\study_code\\Day_19" + file):
        print("文件夹", file)
    else:
        print("文件", file)
