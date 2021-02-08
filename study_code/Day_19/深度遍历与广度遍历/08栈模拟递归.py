myStack = []
data = 0
myStack.append(5)
while len(myStack) != 0:
    num = myStack.pop()
    print(num)
    data += num
    if num == 0:
        print(data)
        break
    else:
        myStack.append(num - 1)
