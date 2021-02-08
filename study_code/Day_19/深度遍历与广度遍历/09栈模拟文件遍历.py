import os

myStack = []
path = "D:\\code\\py\\study_code\\Day_19"
myStack.append(path)

while len(myStack) != 0:
    path = myStack.pop()
    fileList = os.listdir(path)
    for file in fileList:
        filePath = os.path.join(path, file)
        if os.path.isdir(filePath):
            print("文件夹", file)
            myStack.append(filePath)
        else:
            print("文件", file)
