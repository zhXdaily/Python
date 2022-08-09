"""
str1 = 'abcdefg'
print(str1[0])  # a
"""

'''
# 切片
# 语法---> 序列[开始位置下表:结束位置下表:步长]
str1 = '0123456789'
print(str1[2:5])  # 234  步长不写默认1
print(str1[2:5:1])  # 234
print(str1[2:5:2])  # 24
print(str1[:5])  # 01234  开始不写默认0
print(str1[:])  # 0123456789  开始结束都不写打印全部 开始默认0 结束默认结尾 步长默认1
print(str1[::-1])  # 9876543210  步长写负数倒序打印
print(str1[-4:-1]) # 678  下表为负数 -1表示最后一个数据 一次再向前类推 打印时不包含-1的位置

# 如果选取方向和步长方向冲突 则无法选取数据
# print(str1[-4:-1:-1])  # 不能选取数据 从-4开始到-1结束 选取方向从左到右 但是步长为-1 方向从右到左
print(str1[-1:-4:-1])  # 987
'''

'''
# 字符串查找
# 1.find
# 语法   字符串序列.find(子串， 开始位置下标, 结束位置下表)
myStr = 'hello world and itcast and python'
print(myStr.find('and'))  # 12
print(myStr.find('and', 15, 30))  # 23
print(myStr.find('ands'))  # -1表示要查找的字符串不存在

# 2.index
print(myStr.index('and'))  # 12ex查找不存在的字符串会报错  substring not found

# 3.count
print(myStr.count('and', 15, 30))  # 1
print(myStr.count('and'))  # 2
print(myStr.index('and', 15, 30))  # 23
# print(myStr.index('ands'))  # ind
print(myStr.count('ands')) 
# 4.
print(myStr.rfind('and'))  # 23
'''

# 字符串修改rfind
# #  # 0
# 从右侧开始查找
# 1.replace
# 语法  字符串序列.replace(旧子串,新子串,替换次数)
myStr = 'hello world and itcast and python'
print(myStr.replace('and', 'he', 10))

# 2.split
# 语法  字符串序列.split(分割字符, num)
print(myStr.split('and'))  # ['hello world ', ' itcast ', ' python']
print(myStr.split('and', 1))  # ['hello world ', ' itcast and python']

# 3.join  合并列表里的字符串为一个大字符串
newStr = ['aa', 'bb', 'cc']
print('...'.join(newStr))  # aa...bb...cc
