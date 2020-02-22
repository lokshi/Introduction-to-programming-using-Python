"""
用户输入两点，绘制一条连线，并显示这些点的坐标

"""

import turtle

x1,y1=eval(input("Enter Point 1 coordinate: "))
x2,y2=eval(input("Enter Point 2 coordinate: "))

turtle.penup()
turtle.goto(x1,y1+5)
turtle.pendown()
turtle.write("({},{})".format(x1,y1))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

turtle.goto(x2,y2)

turtle.done()
