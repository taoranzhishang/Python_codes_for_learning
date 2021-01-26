'''
mydict={}
print(type(mydict))
'''

mydict = {"abcdefg": 10, "123456": 36, "123456": 136}  # "abcdef"为key不可重复重复被覆盖，10为次数
print(mydict)  # key重复，次数少的会被多的覆盖，{'abcdef': 10, '123456': 136}
print(mydict["abcdefg"])  # 根据key取出value

for key in mydict.items():  # 组合,每一个key和value映射,返回元组
    print(key, type(key))
    '''
    ('abcdefg', 10) <class 'tuple'>
    ('123456', 136) <class 'tuple'>
    '''

for key in mydict:  # 遍历每一个key,遍历字典只会遍历key
    print(key, mydict[key])
    '''
    abcdefg 10
    123456 136
    '''
