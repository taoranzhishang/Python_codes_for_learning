file = open("file", 'r',encoding='utf-8')
counter = 1

for line in file:
    if line[0] != '#':
        print("第%d行" % (counter), line)
        counter += 1
    else:
        pass
