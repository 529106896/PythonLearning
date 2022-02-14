# 猜拳小游戏
# 0石头 1剪刀 2布
import random
count = 0
while count < 10:
    person = int(input("请出拳："))
    computer = random.randint(0, 2)  # 让计算机产生0-2的随机数
    print("你出的是%d，电脑出的是%d" % (person, computer))
    if person == 0 and computer == 1:
        print("你赢了")
    elif person == 1 and computer == 2:
        print("你赢了")
    elif person == 2 and computer == 0:
        print("你赢了")
    elif person == computer:
        print("平手")
    else:
        print("你输了")
    count += 1
