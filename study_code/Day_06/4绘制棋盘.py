import turtle

step = 20

for i in range(18):
    turtle.penup()
    turtle.goto(0, step * i)
    turtle.pendown()
    turtle.forward(step * 18)
turtle.left(90)
for i in range(18):
    turtle.penup()
    turtle.goto(step * i, 0)
    turtle.pendown()
    turtle.forward(step * 18)
turtle.hideturtle()
turtle.penup()
turtle.goto(180, 180)
turtle.pendown()
turtle.dot(10, "black")

turtle.done()
