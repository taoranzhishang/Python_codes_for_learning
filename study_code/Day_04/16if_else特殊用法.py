num = 1
print('a' if num else 'b')  # 满足条件打印a，不满足打印b

num = 10
num = 10 if num > 11 else 20
print(num)

import os

os.system("calc") if num > 21 else os.system("mspaint")
os.system("calc" if num else "mspaint")
