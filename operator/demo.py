"""
# 算数运算符
print(1 + 1)  # 加法运算
print(1 - 1)  # 减法运算
print(2 * 2)  # 乘法运算
print(1 / 2)  # 除法运算
print(11 // 2)  # 整除运算 5
print(11 % 2)  # 取余运算 1
print(2 ** 3)  # 2的3次方 8

print(-9 // -4)  # 2
# 一正一负的整数取整 向下取整 9/4=2.2 向下取整-3
print(9 // -4)  # -3
print(-9 // 4)  # -3
# 取余公式 余数=被除数-除数*商
print(9 % -4)  # -3  -9-（-4）*（-3）= -3  里面的商-3是向下取整
print(-9 % 4)  # 3

# 赋值运算符
i = 3 + 4
print(i)
a = b = c = 20  # 链式赋值
print(a, id(a))  # id为地址
print(b, id(b))
print(c, id(c))  # 内存地址一样

m = 20
# 参数赋值
m += 30  # a = a + 30
print(m)

# 解包赋值
o, p, q = 20, 30, 40
print(o, p, q)

# 交换赋值
j, k = 10, 20
print('交换之前：', j, k)
j, k = k, j
print('交换之后：', j, k)

# 比较运算符
# 结果为bool类型
a, b = 10, 20
print('a > b吗', a > b)  # a > b吗 False
print('a < b吗', a < b)  # a < b吗 True

# 比较对象的标识使用is
e = 10
f = 10
print(e == f)  # True 说明e与f的value相等
print(f is f)  # True 说明e与f的id标识相等
print(id(e), id(f))  # 2812245994064 2812245994064

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False
print(lst1 is not lst2)  # True
"""

'''
# bool运算符
a, b = 1, 2
# and 与运算
print(a == 1 and b == 2)  # True
# or 或运算
print(a == 1 or b > 2)  # True
# 取反
f1 = False
f2 = True
print(not f1)
print(not f2)

s = 'helloworld'
print('w' in s)  # True
print('k' in s)  # False
print('w' not in s)  # False
print('k' not in s)  # True
'''

# 位运算
# 二进制
print(4 & 8)  # 按位与00000100 & 00001000 = 00000000
print(4 | 8)  # 按位或                    = 00001100 = 12
# 左移一位 相当于乘以2
print(4 << 1)  # 向左移动1个位置 00000100 << 1   00001000 = 8
# 右移一位 相当于除以2
print(4 >> 1)  # 向右移动一个位置 00000100 >> 1    00000010 = 2
