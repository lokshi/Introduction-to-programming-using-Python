"""
计算利息
利息 =  差额 X （年利率 /　1200）

"""

balance,interestRate = input('Enter balance and interest rat (e.g,3 for 3%): ').split(",")
balance=int(balance)
interestRate=float(interestRate)

# interest=round((balance * (interestRate / 1200)),5)


print("The interest is {}".format(round((balance * (interestRate / 1200)),5)))