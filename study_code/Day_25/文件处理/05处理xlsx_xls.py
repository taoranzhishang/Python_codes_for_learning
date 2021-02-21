from collections import OrderedDict  # 不可变字典
# pip install  pyexcel
from pyexcel_xls import get_data  # 读取数据
from pyexcel_xls import save_data  # 写入数据


def readxls():
    path = r"C:\Users\Tsinghua-yincheng\Desktop\day24down\doc\1.xlsx"
    xlsdata = get_data(path)  # 抓取数据
    print(xlsdata)
    print(type(xlsdata))  # 字典类型
    for sheet in xlsdata:  # 读取每个key-value
        print(sheet, ":", xlsdata[sheet])


def writexls():  # 写入excel
    path = "myself.xls"
    data = OrderedDict()  # 字典
    sheet_1 = []  # 表格
    sheet_2 = []  # 表格
    row1 = ["A", "B", "C"]
    row2 = [1, 2, 3]
    sheet_1.append(row1)
    sheet_1.append(row2)
    sheet_2.append(row1)
    sheet_2.append(row2)

    data.update({"ABC": sheet_1})
    data.update({"XYZ": sheet_2})
    save_data(path, data)


writexls()
# readxls()
