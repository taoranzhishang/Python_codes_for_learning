class filegetlines:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, "rb")
        self.Lines = -1

    def readlines(self):
        i = 0
        while True:
            linestr = self.file.readline()
            if linestr:  # 不为空，
                print(linestr)
                i += 1
            else:
                # 为空
                break
        self.Lines = i
        return i


f1 = filegetlines(r"C:\Users\Tsinghua-yincheng\Desktop\day14down\code\pass1.txt")
print(f1.readlines())
f2 = filegetlines(r"C:\Users\Tsinghua-yincheng\Desktop\day14down\code\pass2.txt")
print(f2.readlines())

'''

lines=10
i=1
file=open(r"C:\Users\Tsinghua-yincheng\Desktop\day14down\code\pass1.txt","rb")
while i<lines:
    linestr=file.readline()
    print(linestr)
    i+=1
'''
