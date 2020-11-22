import turtle

turtle.screensize(500, 500)  # 调整屏幕大小x,y
turtle.write("你好天朝", font=("华文行楷", 20, "normal"))  # 字体，大小
turtle.circle(100)
turtle.circle(100, steps=3)  # 画一个环形，steps参数最小为1，1是一个点，2是往返的线，3是三角……

'''
turtle.begin_fill()#开始填充
turtle.circle(100,steps=3)
turtle.circle(100)
turtle.color("red")#设置颜色
turtle.end_fill()#结束填充

turtle.reset()#重置
turtle.pensize(10)#画笔大小
turtle.hideturtle()#隐藏箭头

turtle.begin_fill()
turtle.circle(100,steps=5)
turtle.color("blue")
turtle.end_fill()

'''

turtle.exitonclick()
