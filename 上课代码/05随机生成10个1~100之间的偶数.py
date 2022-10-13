print('---------------- 随机产生10个100以内的偶数 ----------------')
import random  # 导入random模块

k = 0  # 初始化
while True:
    n = random.randint(1, 101)
    if n % 2 == 0:  # 除二取余值为0的话，就是偶数
        print('随机生成的第{:3d}个偶数为：{:3d}！'.format(k + 1, n))
        k += 1  # 记录产生偶数的个数
    if k == 10:  # 若产生了十个偶数，则跳出循环
        break
