import turtle
import math

r = input("请输入半径：")
r = eval(r)
area = 5 * r * r / math.tan(math.pi / 5) / 4

turtle.circle(r, steps=5)
turtle.penup()
turtle.goto(0, r)
turtle.pendown()
turtle.write(str(area))  # turtle.write函数只能输出字符串

turtle.exitonclick()
