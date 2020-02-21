"""
Turtle 绘制四个圆

"""
import turtle,time

radius = eval(input("Enter the radius: "))

turtle.color("blue")
turtle.penup()
turtle.goto(-(radius),0)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(radius,0)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(-(radius),-radius*2)
turtle.pendown()
turtle.circle(radius)

turtle.color("black")
turtle.penup()
turtle.goto(radius,-radius*2)
turtle.pendown()
turtle.circle(radius)


time.sleep(5)