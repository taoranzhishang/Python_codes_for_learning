import os

"""
广度遍历
"""
def getFileTree(path, treeTab):
    fileList = os.listdir(path)
    for file in fileList:
        filePath = os.path.join(path, file)
        if os.path.isdir(filePath):
            print("文件夹", file)
            treeTab += '  '
            getFileTree(filePath, treeTab)
        else:
            print(treeTab + "文件", file)


getFileTree(r"/study_code/Day_16", '')
