def func():
    print("func")


print("test")
if __name__ == "__main__":
    print(__name__)  # __main__
"""
作为执行模块时，全部执行
作为调用模块时，选择执行，判断语句不执行，其余在调用时会全部执行一遍
"""
