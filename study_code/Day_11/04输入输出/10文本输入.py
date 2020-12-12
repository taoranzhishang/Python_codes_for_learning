import os

# 文本重定向
# python 10文本输入.py < myCmd.txt > output.txt
# >覆盖写入，>>追加写入
myCmd = input("Please enter:")
os.system(myCmd)
