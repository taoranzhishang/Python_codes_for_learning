single_price = 28
double_price = 68
triple_price = 99
family_price = 168


def cost_calc(menu, quantity):
    cost = 0

    if menu == '1':
        cost = quantity * single_price
    elif menu == '2':
        cost = quantity * double_price
    elif menu == '3':
        cost = quantity * triple_price
    elif menu == '4':
        cost = quantity * family_price

    return cost


def main():
    menu = input("请选餐（'1'为单人餐，'2'为双人餐，'3'为三人餐，'4'为全家福）：")#输入商品序号
    quantity = eval(input("请输入数量："))#输入商品数量
    totalCost = cost_calc(menu, quantity)#调用函数，将
    print("您本次需支付：%d元" % totalCost)


if __name__ == "__main__":
    main()
