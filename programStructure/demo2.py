"""
money = 1000
s = int(input('请输入取款金额'))
if s <= money:
    money = money - s
    print('取款成功，余额为：', money)
else:
    print('余额不足')
"""

# range函数 同于生成一个整数序列
# range的三种创建方式
r1 = range(10)
print(r1)  # range(0, 10)
print(list(r1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  list用于查看range中的整数序列

r2 = range(1, 6)  # 指定了开始和停止
print(list(r2))  # [1, 2, 3, 4, 5]

r3 = range(1, 7, 2)  # 指定了开始 停止 步长
print(list(r3))  # [1, 3, 5]

