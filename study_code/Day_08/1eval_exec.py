import os

print(eval("1*2"))
# print(eval(1*2))#eval只能处理字符串

exec("print(\"hello world\")")  # 字符串，文本当作语句执行
exec("os.system('calc')")  # 成对的引号用于区分
exec("os.system(\"calc\")")  # 转义字符转换
exec("print(1+2)")
