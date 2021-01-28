import itertools

pwd = ("".join(x) for x in
       itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=16))
print(type(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
print(next(pwd))
