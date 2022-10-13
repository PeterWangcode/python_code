print('----------------实现一元二次方程的求解----------------')

import math  # 调用math模块

a = float(input('输入数值a：'))
b = float(input('输入数值b：'))
c = float(input('输入数值c：'))

d = b * b - 4 * a * c  # 将 b * b - 4 * a * c 赋给d
if (a == 0):  # a=0不是一元二次方程
    print('a等于零，该方程不是二元一次方程')
else:  # a!=0时，一元二次方程成立
    if (d >= 0):  # b*b-4ac>=0，有两个解
        x1 = (-b + math.sqrt(d)) / 2 * a  # 加的情况
        x2 = (-b - math.sqrt(d)) / 2 * a  # 减的情况
        print('x1的值为：{}\nx2的值为：{}'.format(x1, x2))
    else:  # b*b-4ac<0，方程无解
        print('该方程无解')
