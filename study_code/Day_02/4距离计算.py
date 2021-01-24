import turtle as t

x1, y1 = eval(input("enter x1 and y1 for point 1:"))
x2, y2 = eval(input("enter x2 and y2 for point 2:"))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
t.showturtle()
t.penup()
t.goto(x1, y1)
t.write("point 1:" + str(x1) + ',' + str(y1))
t.pendown()
t.goto(x2, y2)
t.write("point 2:" + str(x2) + ',' + str(y2))

t.penup()
t.goto((x1 + x2) / 2, (y1 + y2) / 2)
t.write("distance=" + str(distance))  # turtle.write()只能打印字符串

t.exitonclick()
