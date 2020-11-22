str = "1\t2\t3"
print(str.expandtabs(tabsize=2))  # 将\t转换为空格，默认一个\t转8个空格，tabsize指定数量
print(str.expandtabs())