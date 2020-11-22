# print默认结束后换行

print('a', end="")  # 不换行，以空结尾
print('a', end="")
print('a', end=" ")  # 默认以引号内容结尾

print(1, 2, 3)  # 逗号分隔，默认以空格隔开
print(1, 2, 3, sep="")  # 以空隔开
print(1, 2, 3, sep="*")  # 以*隔开
