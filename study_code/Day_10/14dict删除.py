mydict={"abcd":12,"efg":10}

print(mydict)
del mydict["efg"]#删除一个
print(mydict)

mydict.clear()#清空，仍可以引用，
print(mydict)

del mydict#删除全部，内存回收，引用报错
