"""
STOP 警告牌

"""

import turtle

turtle.pensize(3)

turtle.penup()
turtle.goto(-200,0)
turtle.right(90)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(200, steps = 6) # Draw a hexagon
turtle.end_fill()

turtle.color("white")
turtle.penup()
turtle.goto(-130, -65)
turtle.pendown()
turtle.write("STOP",
  font = ("Times", 80, "bold"))

turtle.hideturtle()


turtle.done()
