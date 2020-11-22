import turtle

step = 20
for i in range(8):
    for j in range(8):
        turtle.penup()
        turtle.goto(i * step, j * step)
        turtle.pendown()
        turtle.begin_fill()
        if (i + j) % 2 == 0:
            turtle.color("white")  # i+j为偶数时设置为白色，奇数设置为黑色
        else:
            turtle.color("black")
        for k in range(4):
            turtle.forward(step)
            turtle.right(90)
        turtle.end_fill()

turtle.done()
