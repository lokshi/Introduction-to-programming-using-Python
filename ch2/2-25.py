"""
Turtle 绘制一个矩形

"""
import turtle,time

x,y,a,b=input("Enter x y a and b in the rectangle: ").split(",")


x=float(x)
y=float(y)
a=float(a)
b=float(b)

turtle.color("blue")
turtle.penup()
turtle.goto(x-(a/2),(y-(b/2))
# turtle.goto(x,y)
turtle.pendown()
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)

time.sleep(5)