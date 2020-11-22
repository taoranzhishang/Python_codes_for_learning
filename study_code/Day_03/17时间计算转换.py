seconds = eval(input("please input time:"))
minutes = seconds // 60
days = minutes // (60 * 24)
# months=days//30
years = days // 365
days //= 365
minutes //= (60 * 24)
seconds //= (60 * 60 * 24)
print(str(years) + 'years', str(days) + 'days', str(minutes) + 'minutes', str(seconds) + 'seconds')
