"""
估算面积

广州大概定点：(23.900,113.922)(23.430,112.975)(22.529,113.680)(23.228,113.892)

"""

import math

x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))
x3, y3 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))
x4, y4 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

x1 = math.radians(x1)
x2 = math.radians(x2)
x3 = math.radians(x3)
x4 = math.radians(x4)
y1 = math.radians(y1)
y2 = math.radians(y2)
y3 = math.radians(y3)
y4 = math.radians(y4)

d1 = 6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
d2 = 6371.01 * math.acos(math.sin(x1) * math.sin(x4) + math.cos(x1) * math.cos(x4) * math.cos(y1 - y4))
d3 = 6371.01 * math.acos(math.sin(x3) * math.sin(x2) + math.cos(x3) * math.cos(x2) * math.cos(y3 - y2))
d4 = 6371.01 * math.acos(math.sin(x3) * math.sin(x4) + math.cos(x3) * math.cos(x4) * math.cos(y3 - y4))
d5 = 6371.01 * math.acos(math.sin(x1) * math.sin(x3) + math.cos(x1) * math.cos(x3) * math.cos(y1 - y3))

s1 = (d1 + d3 + d5) / 2
s2 = (d2 + d4 + d5) / 2

area = math.sqrt(s1 * (s1 - d1) * (s1 - d3) * (s1 - d5)) + math.sqrt(s2 * (s2 - d2) * (s2 - d4) * (s2 - d5))

print("广州市面积大约：{} 平方公里".format(round(area,2)))
