import os

pid = os.fork()  # fork反复拷贝
if pid == 0:
    print("A", os.getpid(), os.getppid())
else:
    print("B", os.getpid(), os.getppid())

pid = os.fork()
if pid == 0:
    print("C", os.getpid(), os.getppid())
else:
    print("D", os.getpid(), os.getppid())
