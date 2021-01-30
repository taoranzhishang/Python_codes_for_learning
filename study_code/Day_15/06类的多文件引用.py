import sys

# sys.path.append(r"D:\code\py\study_code\Day_15")
print(sys.path[0])
# del sys.path[0]
print(sys.path)

# import test
# run=test.TestClass()
# run.test()
sys.path.append(r"D:\code\py\study_code\Day_15")
print(sys.path)

from test import TestClass  # 没有导入成功

run = TestClass()
run.test()
