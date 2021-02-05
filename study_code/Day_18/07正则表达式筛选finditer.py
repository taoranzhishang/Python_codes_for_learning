import re

for data in re.finditer("\\d+", "abc232daf13451cz3456ddaA3D56FN"):  # 筛选提取数字
    print(data.group())

for data in re.finditer("[A-Za-z]", "abc232daf13451cz3456ddaA3D56FN"):  # 筛选提取字母
    print(data.group())

for data in re.finditer("[反清复明]", "abc232da反f1清3451cz复明3456ddaA3D56FN"):  # 筛选提取……
    print(data.group())

for data in re.finditer("[^反清复明]", "abc232da反f1清3451cz复明3456ddaA3D56FN"):  # 筛选去除……
    print(data.group())
