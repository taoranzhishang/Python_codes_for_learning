import time
import os

num = 1
'''
while 1:
    time.sleep(1)
    print('第'+str(num)+'秒')
    num+=1
    if num==5:
        os.system("start notepad")
    elif num==10:
        os.system("taskkill /f /im notepad.exe")
    elif num>10:
        break
'''

for i in range(1, 11):
    time.sleep(1)  # 每循环一次，sleep1秒
    # print('第'+str(num)+'秒')
    print("第%d秒" % num)
    num += 1
    if num == 5:
        os.system("start notepad")
    elif num == 10:
        os.system("taskkill /f /im notepad.exe")
    elif num > 10:
        break
