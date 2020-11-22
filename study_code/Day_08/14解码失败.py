print("你好中国".encode("utf-8"))
print(("你好中国".encode("utf-8").decode("gbk", "ignore")))  # 解码失败，强行解码，忽略错误
print(("你好中国".encode("utf-8").decode("utf-8", "ignore")))  # 若有错误，忽略错误，没有错误，正常解码
