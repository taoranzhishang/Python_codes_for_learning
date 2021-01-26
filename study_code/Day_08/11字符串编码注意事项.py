# 不同的编码格式，大小不同，，内容不同
print(bytes('a',"utf-8"))
a = bytes(1)  # bytes转换为二进制编码，占1字节
print(a)  # \x 16进制，1byte，8bite
b = bytes("你好天朝", "utf-8")  # 转换成二进制编码，utf-8编码格式
print(b)
c = bytes("你好天朝", "gbk")  # gbk编码格式
print(c)
# b'  bytes类型
print(bytes("我", "utf-8"))  # b'\xe6\x88\x91'utf-8一个汉字3字节
print(bytes("我的", "utf-8"))  # b'\xe6\x88\x91\xe7\x9a\x84'
print(bytes("我的啊", "utf-8"))  # b'\xe6\x88\x91\xe7\x9a\x84\xe5\x95\x8a'

print(bytes("我", "gbk"))  # b'\xce\xd2'gbk一个汉字两个字符
print(bytes("我的", "gbk"))  # b'\xce\xd2\xb5\xc4'
print(bytes("我的啊", "gbk"))  # b'\xce\xd2\xb5\xc4\xb0\xa1'
