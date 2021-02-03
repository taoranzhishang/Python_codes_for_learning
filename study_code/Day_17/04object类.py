"""
所有的类都有一个基类object
"""


class OBJ1:
    pass


class OBJ2(object):
    pass


o1 = OBJ1()
o2 = OBJ2()
print(dir(o1))
print(dir(o2))
print(dir(object))
