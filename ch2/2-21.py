"""
复利值
年利率：5% ，月利率：0.05 /12=0.00417
"""

saveAmount = float(input("Enter the monthly saving amount: "))
mons = 0
moneys = 0
while mons < 6:
    moneys = (saveAmount + moneys) * (1 + 0.00417)
    mons += 1

print("After the sixth month, the account value is {}".format(round(moneys,2)))