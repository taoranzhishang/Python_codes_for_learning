# print("hello world")
# str1="str"
# str2="str"
# print(id(str1),id(str2))
#
#
# name="bob"
# age=1
# print("name is %s,age is %d"%(name,age))
#
#
# print(4+10%3+20//3**2)
#
#
# str = "hello world"
# str_son ="lo"
# print(str_son in str)
#
# print(3-3 and 6)
#
# print(2+3 or None)
#
#
# a=10
# b =3
# if a!=b:
#     print(a*3)
# else:
#     print(a+2)
# print(a)
#
# a=10
# b =3
# if a!=b:
#     a+=b
# else:
#     a%=b
# str="世界那么大，我想去看看"
# print(str[7,-3])
# print(5+4j>2-3j
# print(pow(2,10))
# x=1
# y=2
# min = x if x < y else y
# x=0
# while x<3:
#     #if x<3:
#     print(x)
#     x+=1
#     # else:
#     #     break
# else:
#     print("*")

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     break  # 对里面的这个while起作用
#         # continue
#
#     print("")  # 换行
#
#     i += 1
#     break  # 最外边的while起作用

# def func(a,b):
#     return a>>b
# s = func(5,2)
# print(s)
# list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print(list_color[-1]+list_color[2])
# tup1 = 'a',
# print(type(tup1))

# tup1 = ('154', '203', '043', 'black', 'blue','red')
# print(min(tup1))
# list1 = [1,3,6,7]
# print(list1.pop())
# mydict={(1):1}
# mydict.clear()
# print(mydict)
#
# dict2 = {'Name': 'Orange', 'Color': 'Orange', 'Count': 4}
# print("Name" in dict2)
# dict3=dict2.copy()
# del dict2["Name"]
# print(dict3)
# set1={1}#字典类型
# print(type(set1))

# set0={1,3,4,5,6}
# print(set0[2])
# str='123"134"14'
#

# print("123 abc".isdecimal())
# if []:
#     print("*")
# s=(100, 'word', 10.5)
# print(type(s))

# x = 1
# y = 2
# z = 1
# x = (y = z - 1)
# x += y??x = x + y

# print (100 - 25 * 3 % 5)
# str2="你是谁？他从哪里来？谁要到哪去？"
# print(str2.replace("你", "我").replace("他", "我").replace("谁", "我"))
# print(str2.replace("你", "我").replace("他", "我").replace("谁要到哪去", "我要到哪去"))
# print(str2.replace("你", "我") ,("他", "我"), ("谁", "我"))
# print(str2.replace("你", "我"), ("他", "我"), ("谁要到哪去", "我要到哪去"))

# from os import *
#
# a= [1,2,3,None,0,[],"py"]
# print(len(a))
# print(type([1, 2, 3,"tuple"]))
# y=30-3**2+8//3**2*10
# print(y)
# print(type({5}))
# s='python123'
# print(s[2:4])
# 等级='优秀'
# print(等级)

# x=4
# print(round(x, 3))
# print(f'{x:.3f}')
# print('{:.3f}'.format(x))
# s=0
# for i in range(1,6,2):
#     if i<5:
#         print(i,end='+')
#         s=s+i
#     else:
#         s=s+i
#     print(i,end='=')
# print(s)

# try:
#     1/0
# except:
#     print('something wrong happened..')
# finally:
#     print('it seems i cannot be with except')
# l=[1,2,3]
# print(l[3])

# n = 2
#
# def multiply(x, y=10):
#     global n
#     return x * y * n
# s = multiply(10, 2)
# print(s)

# def split(s):
#     return s.split("a")
# s = "Happy birthday to you!"
# print(split(s))
# print(0.1**0.3)
# print(1001 == 0x3e7)
# def convert(n,k):
#     if n>0:
#         return convert(n//k,k)+str(n%k)
#     else:
#         return ''
# a,b=eval(input())
# print(convert(a,b))
# x=['令狐冲','林平之','任盈盈','岳灵珊']
# f=open('武侠人物传.txt','w')
# f.write(' '.join(x))
# f.close()

# print(format(10))
# tp=1,2,3
# print(type(tp))
# def func(num):
#     num *= 2
# x = 20
# func(x)
# print(1.23e-4 + 5.67e+8j.real)
# a=1.234
# a=int(a)
# print(type(a),a)
# print(3 or(0 and 4))
# s=set()
# print(type(s))
# print(type({}))
# # dict3 = {(1,2,3):"uset"}
# dict2 = {}
# dict3 = {(1,2,3):"uestc"}
# print(type(dict3))
# tup1 = ('154', '203', '043', 'black', 'blue','red')
# print(min(tup1))
# print (100 - 25 * 3 % 5)
# print(type({5}))