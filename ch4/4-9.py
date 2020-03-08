"""
比较价钱
"""
weight1,price1=eval(input("Enter weight and price for package1: "))
weight2,price2=eval(input("Enter weight and price for package2: "))

package1=price1/weight1
package2=price2/weight2

if package1 > package2:
    print("Package 2 has the better price.")
else:
    print("Package 1 has the better price.")

