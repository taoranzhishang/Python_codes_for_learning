import os

"""
popen()与system()可以执行指令
popen()可以获取执行后返回的结果，一个文件读取的对象，system()不可以
"""
str1 = os.popen("notepad")
print(str1)  # <os._wrap_close object at 0x000001D9DAA89670>
# str1=str1.read()
# print(str1)

str2 = os.popen("ipconfig")
print(str2)  # <os._wrap_close object at 0x000001DE3321A1C0>
str2 = str2.read()  # 读取命令行的输出
print(str2)

str3 = os.popen("tasklist")
str3 = str3.read()
if str3.find("TIM.exe") != -1:
    print("TIM正在运行")
else:
    print("TIM未在运行")
