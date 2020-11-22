year = eval(input("please input year:"))
month = eval(input("please input month:"))
day1 = 30
day2 = 31
day3 = 29
day4 = 28

if (month > 0 and month <= 7 and month != 2 and month % 2 == 1) \
        or (month >= 8 and month <= 12 and month % 2 == 0):
    print(day2)
elif (month > 0 and month <= 7 and month != 2 and month % 2 == 0) \
        or (month >= 8 and month <= 12 and month % 2 == 1):
    print(day1)
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) \
            or (month != 2 and month >= 8 and month % 2 == 0):
        print(day3)
    # elif year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
    #     print(day3)
    else:
        print(day4)
else:
    print("你脑子进水了")
