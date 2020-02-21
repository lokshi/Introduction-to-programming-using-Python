"""
一个正多边形的面积

"""

import math

n=eval(input("Enter the number of sides: "))
s=eval(input("Enter the side: "))

area=(n*math.pow(s,2)) / (4* math.tan(3.14/n))

print("The area of the polygon is {}".format(area))
