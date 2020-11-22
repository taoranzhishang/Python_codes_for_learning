coatPrice = 150.00
pantsPrice = 100.00
shoesPrice = 120.00


def cost_calc(list, quantity):
    '''
    计算打折前价格
    计算各商品数量
    '''
    cost = 0.00
    coatQuantity = 0.00
    pantsQunatity = 0.00
    shoesQuantity = 0.00

    for productTemp, quantityTemp in zip(list, quantity):

        if productTemp == '1':
            cost += quantityTemp * coatPrice
            coatQuantity += quantityTemp

        if productTemp == '2':
            cost += quantityTemp * pantsPrice
            pantsQunatity += quantityTemp

        if productTemp == '3':
            cost += quantityTemp * shoesPrice
            shoesQuantity += quantityTemp


    else:
        return cost, coatQuantity, pantsQunatity, shoesQuantity


def sale_calc(totalCost, coatQuantity, pantsQunatity, shoesQuantity):
    '''
    计算打折后价格
    计算商家利润
    '''
    cost = 0
    profits = 0
    if totalCost < 100.00:
        cost = totalCost
        profits = cost - (coatQuantity * 100.00 + pantsQunatity * 80.00 + shoesQuantity * 90.00)
    elif 100.00 <= totalCost < 200.00:
        cost = totalCost - 5
        profits = cost - (coatQuantity * 100.00 + pantsQunatity * 80.00 + shoesQuantity * 90.00)
    elif 200.00 <= totalCost <= 400.00:
        cost = totalCost * 0.95
        profits = cost - (coatQuantity * 100.00 + pantsQunatity * 80.00 + shoesQuantity * 90.00)
    elif totalCost > 400.00:
        cost = (totalCost - 20.00) * 0.9
        profits = cost - (coatQuantity * 100.00 + pantsQunatity * 80.00 + shoesQuantity * 90.00)
    return cost, profits


def main():
    '''
    主函数
    实现商品的种类以及数量的接收
    '''

    cusList = []
    cusQuantity = []
    totalCost = 0
    print("""🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁
🎁🎁🎁🎁好消息！好消息！🎁🎁🎁🎁
🎁🎁🎁🎁天府商场发福利！🎁🎁🎁🎁
🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁
100元不打折，100-200元之间减5元，200-400元之间打95折
如果超过400元，则满400-20的基础上再打九折！！！
    """)
    while True:
        '''
        商品输入，1为上衣，2为裤子，3为鞋子
        输入不满足要求则不添加到cusList，并重新循环
        '''
        product = input("请输入商品序号（1为上衣，2为裤子，3为鞋子）：")

        if product == '1' or product == '2' or product == '3':
            cusList.append(product)
        else:
            print("您的输入不符合系统要求,请重新输入！")
            continue

        '''
        商品数量输入，输入必须为数字，不满足要求则不会添加到cusQuantity，并且pop掉cusList
        '''
        quantity = input("请输入您的商品数量：")

        if quantity.isdigit():
            cusQuantity.append(eval(quantity))
        else:
            print("您的输入不符合系统要求,请重新输入！")
            cusList.pop()
            continue

        '''
        输入'C'继续选择，'R'重新选择，其它任意字符结束选择
        '''
        command = input("输入'C'继续选择，'R'重新选择，其它任意字符结束选择：")

        if command == 'C' or command == 'c':
            continue
        elif command == 'R' or command == 'r':
            cusList.clear()
            cusQuantity.clear()
            print("订单已取消，请重新选择！")
        else:
            break

    totalCost, coatQuantity, pantsQunatity, shoesQuantity = cost_calc(cusList, cusQuantity)  # 计算初始价格
    saleCost, saleProfits = sale_calc(totalCost, coatQuantity, pantsQunatity, shoesQuantity)  # 计算打折价格和商家利润

    if coatQuantity or pantsQunatity or shoesQuantity:
        print("此次的订单为，")
        if coatQuantity:
            print("上衣：%d件" % coatQuantity)
        if pantsQunatity:
            print("裤子：%d条" % pantsQunatity)
        if shoesQuantity:
            print("鞋子：%d双" % shoesQuantity)

        print("订单已提交，共计支付：%.2f￥\n利润为：%.2f￥" % (saleCost, saleProfits))
    else:
        print("只看不买很费电，适度消费才划算！！！")


if __name__ == "__main__":
    main()
