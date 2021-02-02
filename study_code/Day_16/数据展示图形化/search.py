import codecs
import 数据展示图形化.listdiaplay
import 数据展示图形化.textdiaplay
import 数据展示图形化.tabledisplay


class Search:
    def __init__(self, path, mode):
        self.file = codecs.open(path, "GBK", "ignore")
        self.mode = mode
        self.dataView = None
        if self.mode == "list":
            self.dataView = 数据展示图形化.listdiaplay
        elif self.mode == "text":
            self.dataView = 数据展示图形化.textdiaplay
        else:
            self.dataView = 数据展示图形化.tablediaplay

    def search(self, data):
        while True:
            line = self.file.readline()
            if line.find(data) != -1 and self.dataView != None:
                self.dataView.addData(line)
            if not line:
                break

    def display(self):
        if self.dataView != None:
            self.dataView.display()

    def __del__(self):
        self.file.close()
