num = eval(input("please input:"))
print(num)
max = eval(input("input:"))
print(max)

for i in range(num):
    data = eval(input("input:"))
    if data > max:
        max = data
print(max)
