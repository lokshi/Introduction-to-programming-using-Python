"""
输入三个数，升序排列

"""

a,b,c=eval(input("Enter three number: "))

if a<b:
    temp=a
    a=b
    b=temp
if a<c:
    temp =a
    a=c
    c=temp
if b<c:
    temp=b
    b=c
    c=temp

print("The ascending sort is :",c,b,a)