"""
解一元二次方程

"""

import math

a, b, c = eval(input("Enter a,b,c :"))
checkPoint = b ** 2 - 4 * a * c

if checkPoint > 0:
    r1 = (-b + math.sqrt(checkPoint)) / (2 * a)
    r2 = (-b - math.sqrt(checkPoint)) / (2 * a)
    print("The roots are {} and {}".format(r1, r2))
elif checkPoint == 0:
    r1 = -b / (2 * a)
    print("The roots is {} ".format(r1))
else:
    print("The equation has no real roots")
