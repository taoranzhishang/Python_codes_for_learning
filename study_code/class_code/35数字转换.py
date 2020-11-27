numList = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '點']
ChineseNum = []
ArabicNum = input("请输入阿拉伯数字：")
'''
阿拉伯数字转换为繁体中文
功能不完善
'''
for temp in ArabicNum:
    if temp == '0':
        ChineseNum.append(numList[0])
    elif temp == '1':
        ChineseNum.append(numList[1])
    elif temp == '2':
        ChineseNum.append(numList[2])
    elif temp == '3':
        ChineseNum.append(numList[3])
    elif temp == '4':
        ChineseNum.append(numList[4])
    elif temp == '5':
        ChineseNum.append(numList[5])
    elif temp == '6':
        ChineseNum.append(numList[6])
    elif temp == '7':
        ChineseNum.append(numList[7])
    elif temp == '8':
        ChineseNum.append(numList[8])
    elif temp == '9':
        ChineseNum.append(numList[9])
    elif temp == '.':
        ChineseNum.append(numList[10])
print(''.join(ChineseNum))
