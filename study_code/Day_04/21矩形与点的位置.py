import turtle
import math

turtle.penup()
turtle.goto(200, 100)
turtle.pendown()

turtle.goto(200, -100)
turtle.goto(-200, -100)
turtle.goto(-200, 100)
turtle.goto(200, 100)

x1, y1 = eval(input("please input pos:"))
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.dot(20, "red")

x1 = abs(x1)
y1 = abs(y1)
if x1 < 200 and y1 < 100:
    print("矩形内")
elif (x1 == 200 and y1 <= 100) or (x1 <= 200 and y1 == 100):
    print("矩形上")
elif x1 > 200 and y1 > 100:
    print("矩形外")

turtle.hideturtle()
turtle.exitonclick()
