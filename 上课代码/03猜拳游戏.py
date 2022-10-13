print('---------------- 猜拳游戏 ----------------')

# 调用函数模块
import random

# 电脑随机出拳
AI = random.randint(0, 2)

# 玩家出拳
print('0:石头/1：剪刀/2：布')
human = int(input('    我出：'))

# 电脑出拳的结果
print('AI出的是：', end='')
if AI == 0:
    print('石头')
elif AI == 1:
    print('剪刀')
elif AI == 2:
    print('布')

# 评判胜负
judge = (human - AI + 3) % 3
if judge == 0:
    print('平局')
elif judge == 1:
    print('很遗憾,您输了！！！')
elif judge == 2:
    print('您取得了胜利！！！')
