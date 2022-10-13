import random

print('{:*^36}'.format('猜数字游戏'))
while True:
    print('请在3次内猜中范围再1~5的数字。')

    stage = 1  # 初始化次数为1
    num = random.randint(1, 6)  # 生成随机数
    while True:
        print(f'第{stage}次输入，正确的数字是：', end='')
        n = int(input())

        if n == num:  # 正确答案
            print(f'答对了！第{stage}次猜中了。')
            break
        elif n > num:
            print('正确答案要小！')
        elif n < num:
            print('正确数字要大！')
        stage += 1
        if stage > 3:
            print(f'真可惜正确数字是{num},游戏结束！')
            break
    k = int(input('(再玩一局：0/结束游戏：1),我选择：'))
    if k == 1:
        break