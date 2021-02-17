import os

print("hello china")
"""
fork()须在Linux下使用
"""
pid = os.fork()  # 复制fork()以下的代码，复制下面的执行代码，独立运行
print("Z")
print("T")
print(pid)  # 进程编号，父进程打开子进程，谁打开子进程谁就是父进程，父进程返回子进程编号，子进程返回编号为0
if pid == 0:
    print("pid==0", "i  am  son")
else:
    print("pid!=0", "i  am  father")
