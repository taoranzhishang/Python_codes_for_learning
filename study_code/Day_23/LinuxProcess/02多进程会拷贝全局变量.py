import os

num = 100  # fork会拷贝全局变量，不冲突，互相独立

pid = os.fork()
if pid == 0:
    num += 100
    print("son", num)
else:
    num += 1000
    print("father", num)
