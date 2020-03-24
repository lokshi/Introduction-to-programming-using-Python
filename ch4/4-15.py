'''
游戏：彩票
随机生成一个三位数，用户输入后:
1、完全匹配，奖金：10,000美元
2、数字全中，奖金：3,000美元
1、1个数字匹配，奖金：1,000美元
'''

import random

chip = 300
print('''
    随机生成一个三位数，你输入后:
        1、完全匹配，奖金：10,000美元
        2、数字全中，奖金：3,000美元
        3、1个数字匹配，奖金：1,000美元
        4、每次投注300美元
''')

while 1:
    print("你现在筹码有{}元".format(chip))
    choice = int(input("你打算：1、不玩了，2、玩"))
    if choice == 1:
        print("哈哈，还算你聪明！")
        break
    else:
        # 随机生成三位数
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
        number3 = random.randint(0, 9)
        number = str(number1) + str(number2) + str(number3)
        print(number)
        g1, g2, g3 = eval(input("请输入你猜的3位数，每位数用逗号隔开: "))
        gnumber = str(g1) + str(g2) + str(g3)

        if gnumber == number:
            print("你中大奖了！10,000元 ")
            chip = chip + 10000
        elif (str(g1) in number) or (str(g2) in number) or (str(g3) in number):
        # elif ((str(g1) in gnumber) and (str(g2) in gnumber) and (str(g3) in gnumber)):
            print("不错，中个3,000元")
            chip = chip +3000
        else:
            print("输了300元")
            chip = chip - 300
