"""
一周的星期几
泽勒的一致性算法
h：一周的星期几（0：星期六；1：星期日......6：星期五）
q：是一个月的哪一天
m：是月份（3：三月；4:四月...... 12：十二月 ）一月和二月都是按照前一年的13月和14月来计算
j：是世纪数（即 year / 100）
k：是一个世纪的某一年（即 year%100）

输入程序显示用户输入一个年份、月份以及这个月的某一天，程序显示它是一周的星期几

"""

years = eval(input("Enter year (e.g., 2008): "))
m = eval(input("Enter month 1-12: "))
q = eval(input("Enter the day of the month 1-31: "))
if m==1 or m==2:
    m=m+12
    years=years-1
j = years // 100
k = years % 100

h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + 5*j) % 7


print("Day of the week is {}".format(h))
