'''
encode将字符串转换为2进制，指定编码方式
decode将2进制编码转换为将字符串，指定编码方式
英文编码无所谓，汉字编码一致，否则出错，乱码
'''
print("你好中国".encode("gbk"))  # b'\xc4\xe3\xba\xc3\xd6\xd0\xb9\xfa'  返回值为二进制
print(b'\xc4\xe3\xba\xc3\xd6\xd0\xb9\xfa'.decode("gbk"))  # 返回值为字符串
print("你好中国".encode("utf-8"))  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9b\xbd'
print(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8"))

print(type("你好中国".encode("gbk")))
print(type("你好中国".encode("utf-8")))
