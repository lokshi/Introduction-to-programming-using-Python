"""

计算三角形周长

"""
s1,s2,s3 = eval(input("Enter the edgs :"))
if (s1+s2)<=s3 or (s2+s3)<=s1 or (s3+s1)<=s2:
    print("The input is invalid")
else:
    perimeters=s1+s2+s3
    print("The perimeter is ：{}".format(perimeters))

