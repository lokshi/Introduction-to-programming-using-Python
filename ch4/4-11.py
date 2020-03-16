"""
找出一个月中的天数

"""

mons, years = eval(input("Enter month and year: "))

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
    month_day[1] = 29

print("{}年{}月有{}天".format(years, mons, month_day[mons-1]))
