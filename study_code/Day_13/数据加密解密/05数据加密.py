sourceFilepath = r"D:\Resources\Python\Python3开发实践真正完整版 尹成大神主讲 代码 + 课件\day13 Python数据切割合并编程\Email.txt"
encryptedFilepath = r"D:\code\py\study_code\Day_13\数据加密解密\encryptedFile.txt"
sourceFile = open(sourceFilepath, 'r')
encryptedFile = open(encryptedFilepath, 'w')

while True:
    ch = sourceFile.read(1)
    if ch:
        encryptedCh = chr(ord(ch) + 1)
        encryptedFile.write(encryptedCh)
    else:
        break

sourceFile.close()
encryptedFile.close()
