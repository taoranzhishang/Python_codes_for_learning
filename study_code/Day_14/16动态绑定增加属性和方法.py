"""
动态绑定，迭代开发
用于对别人写好的类进行额外操作
(lambda x:print(x))(1*2*3)
"""


class Loving:
    pass


loveStory = Loving()
loveStory.boy = "coder"
loveStory.girl = "sb."
loveStory.love = lambda boy, girl: print("%sboy love %s" % (boy, girl))
# loveStory.love = lambda boy, girl: print("%sboy love %s" % (loveStory.boy, loveStory.girl))
# lambda动态增加方法时，参数不能直接使用self，self只能在类方法里面使用,但可以使用对象名
loveStory.love(loveStory.boy, loveStory.girl)
