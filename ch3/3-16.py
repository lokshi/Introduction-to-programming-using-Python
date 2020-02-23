"""
绘制三角形、正方形、五边形、六边形和八边形，要求底边平行于X轴

"""
import turtle

turtle.speed(5)

turtle.color("orange")
turtle.penup()
turtle.goto(-250, 100)
turtle.pendown()
turtle.write("Cool Colourful Shapes",
  font = ("Times", 40, "bold"))

# 三角形
turtle.penup()
turtle.goto(-300,-100)
turtle.right(60)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor("red")
turtle.circle(60, steps = 3) # Draw a hexagon
turtle.end_fill()

# 正方形
turtle.penup()
turtle.goto(-180,-100)
turtle.left(15)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor("green")
turtle.circle(60, steps = 4) # Draw a hexagon
turtle.end_fill()

# 五边形
turtle.penup()
turtle.goto(-50,-100)
turtle.left(9)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(60, steps = 5) # Draw a hexagon
turtle.end_fill()

# 六边形
turtle.penup()
turtle.goto(80,-100)
turtle.left(6)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(60, steps = 6)
turtle.end_fill()

# 八边形
turtle.penup()
turtle.goto(230,-100)
turtle.left(7)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(60, steps = 8)
turtle.end_fill()


turtle.hideturtle()
turtle.done()