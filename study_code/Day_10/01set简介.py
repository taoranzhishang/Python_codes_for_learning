# set为无序不重复的，数值类型默认会升序排列，字符类型乱序
# myset={}  # dict类型
myset = set()  # set类型
print(type(myset))
myset = {1, 2, 3, 4, 5, 4, 3}  # 重新赋值并去除重复
print(myset, type(myset))
