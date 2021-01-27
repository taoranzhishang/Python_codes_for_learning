encryptedFilepath = r"D:\code\py\study_code\Day_13\数据加密解密\encryptedFile.txt"
decryptedFilepath = r"D:\code\py\study_code\Day_13\数据加密解密\decryptedFile.txt"
sourceFile = open(encryptedFilepath, 'r')
decryptedFile = open(decryptedFilepath, 'w')

while True:
    ch = sourceFile.read(1)
    if ch:
        decryptedCh = chr(ord(ch) - 1)
        decryptedFile.write(decryptedCh)
    else:
        break

sourceFile.close()
decryptedFile.close()
