'''
mydict={}
print(type(mydict))
'''

mydict={"abcdefg":10,"123456":36,"123456":136}#"abcdef"为key不可重复重复被覆盖，10为次数
print(mydict)#key重复，次数少的会被多的覆盖，{'abcdef': 10, '123456': 136}
print(mydict["abcdefg"])#根据key取出value

for key in mydict.items():#组合,每一个key和value映射
    print(key)
    '''
    ('abcdefg', 10)
    ('123456', 136)
    '''


for key in mydict:#遍历每一个key
    print(key,mydict[key])
    '''
    abcdefg 10
    123456 136
    '''