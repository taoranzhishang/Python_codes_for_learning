import os

'''
input 输入赋值的是字符串类型，使用要类型转换
'''
str = input("请输入")
print(str)
os.system(str)

num=eval(input("please input a number:"))#input以输入，使用数字要类型转换，eval只处理str了类型，

print(num+1)
