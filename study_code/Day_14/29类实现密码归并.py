# 密码次数排序，假定密码不一样
def merge(path1, path2, path3):
    file1 = open(path1, "rb")
    file2 = open(path2, "rb")
    file3 = open(path3, "wb")
    lines1 = 9
    lines2 = 9
    i1 = 0
    i2 = 0
    linstr1 = file1.readline()  # 读一行
    linstr2 = file2.readline()  # 读一行
    while i1 < lines1 and i2 < lines2:  # 取file1
        linelist1 = (linstr1.decode("utf-8")).split(' ')
        linelist2 = (linstr2.decode("utf-8")).split(' ')
        if eval(linelist1[0]) > eval(linelist2[0]):
            file3.write(linstr1)
            i1 += 1
            linstr1 = file1.readline()
        elif eval(linelist1[0]) < eval(linelist2[0]):
            file3.write(linstr2)
            i2 += 1
            linstr2 = file2.readline()
        else:  # ==
            file3.write(linstr1)
            file3.write(linstr2)
            i1 += 1
            i2 += 1
            linstr1 = file1.readline()
            linstr2 = file2.readline()

    file1.close()
    file2.close()
    file3.close()


merge(r"C:\Users\Tsinghua-yincheng\Desktop\day14down\code\pass1.txt",
      r"C:\Users\Tsinghua-yincheng\Desktop\day14down\code\pass2.txt",
      r"C:\Users\Tsinghua-yincheng\Desktop\day14down\code\pass12.txt")
