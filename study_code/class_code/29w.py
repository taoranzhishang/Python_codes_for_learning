def char_calc(str):
    counter = 0
    for ch in str:
        counter += 1
    return counter


string = input("请输入一个字符串：")
result = char_calc(string)
print("字符个数为：%d" % result)
