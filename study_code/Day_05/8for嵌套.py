import turtle

for i in range(0, 400, 100):
    for j in range(0, 300, 100):
        turtle.goto(j, i)
        turtle.pendown()
        turtle.write(str(j) + ',' + str(i))
    turtle.penup()
turtle.done()
