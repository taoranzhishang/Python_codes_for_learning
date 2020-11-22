num = input("please input a number")
# 判断语句一定要严谨，左右限制死，不然有bug
num = eval(num)
if num == 0:
    print('零')
elif num == 1:
    print('一')
elif num == 2:
    print('二')
else:
    pass
