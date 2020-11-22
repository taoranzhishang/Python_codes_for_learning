import turtle

x1, y1 = eval(input("请输入圆心坐标："))
r = eval(input("请输入圆的半径："))

turtle.penup()
turtle.goto(x1, y1)
turtle.write(str(x1) + ',' + str(y1))
turtle.goto(x1, y1 - r)
turtle.pendown()
turtle.circle(r)

x2, y2 = eval(input("请输入点坐标："))
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(5, "red")
turtle.write(str(x2) + ',' + str(y2))

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

turtle.goto(x1, y1)
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.pendown()
turtle.write("distance")

if distance < r:
    print("圆内")
elif distance == r:
    print("圆上")
else:
    print("圆外")

turtle.hideturtle()
turtle.exitonclick()
