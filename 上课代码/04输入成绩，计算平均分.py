human = 5  # 输入次数
i, sum = 0, 0  # 初始化
while i < human:
    score = float(input('第{}次输入成绩：'.format(i + 1)))
    sum += score
    i += 1
average = sum / human
print('平均分为：{}'.format(average))