"""
工资表

"""

name=input("Enter employee/'s name: ")
workHours=eval(input("Enter of hours worked in a week: "))
payRate=eval(input("Enter hourly pay rate: "))
tax4FederalRate=eval(input("Enter federal tax withholding rate: "))
tax4StateRate=eval(input("Enter state tax withholding rate: "))

grossPay=payRate*workHours
federalTax=grossPay*tax4FederalRate
stateTax=grossPay*tax4StateRate
totalDeduciton=federalTax+stateTax
netPay=grossPay-totalDeduciton

print('''Employee Name: {} 
Hours Worked: {}
Pay Rate: ${}
Gross Pay: ${}
Deductions:
    Federal Withholding (20.0%): ${}
    State Withholding(9.0%): ${}
    Total Deduction: ${}
Net pay: ${}
'''.format(name,workHours,payRate,grossPay,federalTax,stateTax,totalDeduciton,netPay))