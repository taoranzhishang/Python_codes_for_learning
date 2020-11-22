import turtle

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.pencolor("red")
turtle.goto(0, 200)
turtle.goto(200, 200)
turtle.goto(200, 0)
turtle.goto(0, 0)
turtle.end_fill()

turtle.goto(100, 0)
turtle.goto(100, -50)

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.right(270)
turtle.circle(20, -180)
turtle.goto(100, -50)
turtle.circle(20)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
