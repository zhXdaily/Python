"""
while循环语法
while 条件:
    条件成立要重复的代码
    ......
"""

'''
i = 0
while i < 5:
    print('哈哈哈哈哈哈！！！')
    i += 1  # i = i + 1
'''

'''
# 计算1~100的累加和
i = 1
res = 0
while i <= 100:
    res += i
    i += 1
print(res)
'''

'''
# 计算1~100的偶数和
i = 1
res = 0
while i <= 100:
    if i % 2 == 0:
        res = res + i
    i = i + 1
    # res += i  # 这种方式要i = 2
    # i = i + 2
print(res)
'''

'''
# 循环吃5个苹果 吃完第3个饱了 第4和5个不吃了（不执行）
i = 1
while i <= 5:
    if i == 3:
        print(f'吃了{i}个苹果，吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
'''

'''
i = 1
while i <= 5:
    if i == 3:
        print(f'吃到第{i}个苹果吃到虫子 不吃了')
        i = i + 1
        continue
    print(f'吃了{i}个苹果')
    i = i + 1
'''

'''
# while嵌套
# 循环打印3遍媳妇我错了 在打印我刷完 上面一套惩罚打印3遍
j = 0
while j < 3:
    i = 0
    while i < 3:
        print('媳妇我错了')
        i = i + 1
    print('我刷碗')
    print('一套惩罚结束')
    j = j + 1
'''

'''
# 打印5x5星星
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('* ', end='')
        i = i + 1
    print()
    j = j + 1
'''

'''
# 打印三角形星号
j = 0
while j <= 5:
    i = 0
    while i < j:
        i = i + 1
        print('* ', end='')
    print()
    j = j + 1
'''

'''
# 九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i * j}', end='\t')
        i = i + 1
    print()
    j = j + 1
'''

'''
for循环语法
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
'''

'''
str1 = 'itheima'
for i in str1:
    print(i)
'''

str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
        # continue
    print(i)
else:
    print('循环正常结束执行的else代码')
