'''
2x是ASCII格式，3x utf-8，Unicode格式（utf-8、Unicode8、Unicode16），互联网标准格式utf-8
print(u"aaaa")2x中utf-8要加u，3x中默认utf-8，加不加一样
UTF-8包括ASCII
UTF-8可以编译中文，空间占用更大
ASCII格式无中文可以编译，中文不可以
'''

print("C:\\Users\\taora")  # 没有空格，不用外加双引号再转义，直接转义
print(r"C:\Users\taora")  # r代替转义，特殊处理，节约时间
print(r'C:\Users\taora')
print(r"""C:\Users\taora""")

print(r"\"C:\Users\taora\"")  # 一对双引号不可以直接转换
