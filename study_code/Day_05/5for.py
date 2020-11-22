# i=1
# for i in range(1,10):#1<=i<10，默认步长为1
#     print(i)
# for i in range(1,10,2):#1<=i,10,步长为2
#     print(i)
# for i in range(10):#从0循环到9,默认步长为1
#     print(i)
# for i in range(0,10,2):#从0到9，步长2
#     print(i)
'''
range(min,max,step)#从min到max，不包括max，步长为step
range(max,min,-step)#从max到min，不包括min，步长为-step
只能是整数
'''

for i in range(10):
    print(i)
else:  # 最后一次符合循环条件，结束循环前的最后一次，即将跳出循环
    print(i)
