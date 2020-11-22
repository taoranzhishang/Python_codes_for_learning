import turtle

length = 10
step = 10
num = 0

while num < 5:
    turtle.penup()
    turtle.goto(length * 2, length)
    turtle.pendown()
    turtle.goto(length * 2, -length)
    turtle.goto(-length * 2, -length)
    turtle.goto(-length * 2, length)
    turtle.goto(length * 2, length)
    length += step
    num += 1
else:
    print("ok")
turtle.exitonclick()
