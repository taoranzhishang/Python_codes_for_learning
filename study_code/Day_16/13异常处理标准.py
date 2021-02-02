try:
    file = open(r"C:\Users\Tsinghua-yincheng\Desktop\day16down\tools\1.txt", "rb")
    mystr = file.readline().decode("utf-8")
    mylist = mystr.split(" # ")
    num = eval(mylist[0])  # 转化失败
    print(mystr)
    print(num)
    file.write("12321")
    file.close()

except FileNotFoundError:
    print("文件没有找到")
except NameError:  # 特定的异常
    print("转换失败")
except:  # 除了上述之外的所有异常。
    print("处理其他所有异常")
else:  # 没有异常的情况
    print("没有异常执行这里")
finally:  # 有没有异常，无论如何都执行
    print("有没有异常执行这一句")
