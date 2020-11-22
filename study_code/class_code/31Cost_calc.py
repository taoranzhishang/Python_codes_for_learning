single_price = 28
double_price = 68
triple_price = 99
family_price = 168


def cost_calc(menu, quantity):
    cost = 0
    singleQuantity = 0
    doubleQunatity = 0
    tripleQuantity = 0
    familyQuantity = 0

    for menuTemp, quantityTemp in zip(menu, quantity):

        if menuTemp == 'S' or menuTemp == 's':
            cost += quantityTemp * single_price
            singleQuantity += quantityTemp

        if menuTemp == 'D' or menuTemp == 'd':
            cost += quantityTemp * double_price
            doubleQunatity += quantityTemp

        if menuTemp == 'T' or menuTemp == 't':
            cost += quantityTemp * triple_price
            tripleQuantity += quantityTemp

        if menuTemp == 'F' or menuTemp == 'f':
            cost += quantityTemp * family_price
            familyQuantity += quantityTemp

    else:
        return cost, singleQuantity, doubleQunatity, tripleQuantity, familyQuantity


def main():
    cusMenu = []
    cusQuantity = []
    totalCost = 0

    while True:
        menu = input("请选餐（S为单人餐，D为双人餐，T为三人餐，F为全家福）：")
        if menu in "S,s,D,d,T,t,F,f":
            cusMenu.append(menu)
        else:
            print("您的输入不符合系统要求,请重新输入！")
            continue

        quantity = input("请输入您的订单数量：")
        if quantity.isdigit():
            cusQuantity.append(eval(quantity))
        else:
            print("您的输入不符合系统要求,请重新输入！")
            cusMenu.pop()
            continue

        command = input("输入'C'继续点餐，'R'重新选择，其它任意字符结束点餐：")
        if command == 'C' or command == 'c':
            continue
        elif command == 'R' or command == 'r':
            cusMenu.clear()
            cusQuantity.clear()
            print("订单已取消，请重新选择！")
        else:
            break

    totalCost, singleQuantity, doubleQunatity, tripleQuantity, familyQuantity = cost_calc(cusMenu, cusQuantity)
    if singleQuantity or doubleQunatity or tripleQuantity or familyQuantity:
        print("您此次的订单为，")
        if singleQuantity:
            print("单人餐：%d份" % singleQuantity)
        if doubleQunatity:
            print("双人餐：%d份" % doubleQunatity)
        if tripleQuantity:
            print("三人餐：%d份" % tripleQuantity)
        if familyQuantity:
            print("全家福：%d份" % familyQuantity)

        print("您的订单已提交，您此次共计消费：%.2f￥" % totalCost)
    else:
        print("只看不买也费电，适度消费才划算！！！")


if __name__ == "__main__":
    main()
