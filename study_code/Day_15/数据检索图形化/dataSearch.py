import codecs
import dataDisplay


class DataSearch:
    def __init__(self, path):
        self.file = codecs.open(path, "rb", "UTF-8", "ignore")
        self.data = dataDisplay.DataDisplay()

    def search(self, people):
        while True:
            line = self.file.readline()
            if line.find(people) != -1:  # 找到即插入数据
                self.data.addData(line)
            if not line:  # 为空跳出循环
                break

    def display(self):
        self.data.display()

    def __del__(self):
        self.file.close()
        print("Run over")
