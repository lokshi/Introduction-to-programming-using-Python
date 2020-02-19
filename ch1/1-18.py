"""
绘制五角星
"""

import turtle, time

i = 1

turtle.showturtle()
# turtle.write("Five Star")
turtle.color("red")
while i < 6:
    turtle.forward(150)
    turtle.right(144)
    i += 1


time.sleep(5)
