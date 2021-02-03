import 数据查询.ListShow
import 数据查询.TextShow
import codecs


class bigdatafind:
    def __init__(self, path, howtoshow):
        self.file = codecs.open(path, "rb", "GBK", "ignore")  # 打开文件
        self.howtoshow = howtoshow
        self.showview = None  # 窗体-创建
        if self.howtoshow == "listshow":
            self.showview = 数据查询.ListShow.ListShow()
        elif self.howtoshow == "textshow":
            self.showview = 数据查询.TextShow.Textshow()
        else:
            pass

    def find(self, searchstr):
        while True:
            line = self.file.readline()
            if line.find(searchstr) != -1:
                print(line, end="")  # 显示数据
                # 插入
                if self.showview != None:
                    self.showview.addata(line)  # 显示 多态
            if not line:  # 读不到数据退出
                break

    def show(self):
        if self.showview != None:
            self.showview.show()  # 显示 多态

    def __del__(self):
        self.file.close()


'''
big=bigdatafind("Z:\\F\\第一阶段视频\\20170424\\data\\csdnindexsort.txt","listshow")
big.find("yincheng")
big.show()
'''
