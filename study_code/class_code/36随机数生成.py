import random
'''
生成5个0~10的随机数
借助集合的互异性
'''
num = set()
while (len(num) < 5):
    num.add(random.randint(0, 10))
print(num)
