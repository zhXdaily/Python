"""
print('hrllo word')
age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
long_stu_id = 123456789
print('今年我%d岁' % age)
print('我的名字是%s' % name)
print('我的体重是%.2f公斤' % weight)
print('我的学号是%d' % stu_id)
# %03d 表示输出的整数显示位数 不足以0补全 超出当前位数则原样输出
print('我的学号是%03d' % stu_id)  # 001
print('我的学号是%03d' % long_stu_id)  # 123456789
print('我的名字是%s,今年%d岁了' % (name, age))
print('我的名字是%s,今年%d岁了，明年%d岁' % (name, age, age + 1))
# %s比较强大
print('我的名字是%s 体重是%s 年龄是%s 学号是%s' % (name, weight, age, stu_id))

# f格式化字符串
# 语法  f'{表达式}'
print(f'我的名字是{name}, 今年{age}岁')
"""

"""
# int -- 整型
num1 = 1
print(type(num1))
# float -- 浮点型
num2 = 1.1
print(type(num2))
# str --字符串 数据要带引号
a = 'hello world'
print(type(a))
# bool -- 布尔型
b = True
c = False
print(type(b))
print(type(c))
# list -- 列表
d = [10, 20, 30]
print(type(d))
# tuple -- 元组
e = (10, 20, 20)
print(type(e))
# set -- 集合
f = {10, 20, 30}
print(type(f))
# dict -- 字典/键值对
g = {'name': 'tom', 'age': 18}
print(type(g))
"""

"""
# 数据类型转换
num = input('请输入数字：')
print(num)
print(type(num))  # str
print(type(int(num)))  # int
"""

# if 条件：
#     条件成立执行的代码
#     ......

"""
# 缩不缩进都执行
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码1')
print('这个代码执行吗？')

if False:
    print('条件成立执行的代码1')
    print('条件成立执行的代码1')
# 这个代码没有缩进 不属于if语句块 即和成立条件无关
print('这个代码执行吗？')
"""

"""
age = int(input('请输入您的年龄：'))
if age >= 18:
    print(f'您输入的年龄是{age} 已经成年 可以上网')
else:
    print(f'您输入的年龄是{age}, 小朋友回家写作业去')
"""

"""
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您输入的年龄是{age}岁,童工')
# and逻辑与 or逻辑或
# elif (age >= 18) and (age <= 60): # python这地方和C不一样啊 条件可以恒等写
elif 18 <= age <= 60:
    print(f'您输入的年龄是{age}岁,合法工人')
elif age > 60:
    print(f'您输入的年龄是{age}岁,退休吧 铁子')
"""

"""
money = int(input('请输入带没带钱 1带了 0没带： '))
seat = int(input('请输入有没有空座 1有 0没有： '))
if money == 1:
    print('土豪请上车！！！')
    if seat == 1:
        print('有空座，坐下')
    else:
        print('没空做，站着等....')
else:
    print('朋友 没带钱 跟着跑 跑快点')
"""

"""
import random

player = int(input('请出拳：0--石头 1--剪刀 2--布: '))
compter = random.randint(0, 2)
# print(compter)

if ((player == 0) and (compter == 1)) or ((player == 1) and (compter == 0) or (player == 0) and (compter == 0)):
    print('玩家赢')
elif player == compter:
    print('平局')
else:
    print('电脑获胜')
"""

# 三目运算符
# 从if开始读 if为条件成立的表达式 else为条件不成立的表达式
a = 1
b = 2
c = a if a > b else b
print(c)

# 有两个变量 比较大小 如果变量1大于变量2 执行变量1-变量2 如果变量2大于变量1 执行变量2-变量1
aa = 10
bb = 2
cc = (aa - bb) if (aa > bb) else (bb - aa)
print(cc)
