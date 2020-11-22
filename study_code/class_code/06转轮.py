import turtle
import random


turtle.speed(0)
#turtle.colormode(255)
turtle.pencolor("purple")

for i in range(500):
    #turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.fd(i)
    turtle.right(91)

turtle.mainloop()