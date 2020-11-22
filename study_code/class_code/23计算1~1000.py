# sum=0
# for num in range(1,1001):
#     sum+=num
# print(sum)

# sum=0
# num=1
# while num<=1000:
#     sum+=num
#     num+=1
# print(sum)

# print(list({"adf"   "fdf"}))

#len,str().ord(),lower(),uppper(),isdecimal(),replace(),split()
###############分割线###################
mystr="Hello World"
num=4294967195
print(len(mystr))#求长度
print(str(num))#转换为string
print(ord('A'))#求字符ASCII
print(mystr.lower())#小写转大写
print(mystr.upper())#大写转小写
print(mystr.isdecimal())#字符串只含十进制数字返回True，反之返回False
print(str(num).isdecimal())
print(mystr.replace('l','L'))#字符'l'转换为字符'L'
print(mystr.split(' ',1))#切割间隔的指定字符，次数1次