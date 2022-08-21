# 列表 list
"""
a = 10
lst = ['hello', 'world', 90]
print(id(lst))
print(id(lst[0]))
print(id(lst[1]))
print(id(lst[2]))
print(type(lst))
print(lst)
"""

'''
# 列表的创建
# 方法1
lst = ['hello', 'world', 90]
print(lst)
print(lst[0])  # hello
print(lst[-3])  # hello

# 方法二 使用内置函数list
lst2 = list(['hello', 'world', 90])
'''

'''
# 获取列表元素的索引
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))  # 0  如果查询元素有重复 只返回相同元素第一个索引
# print(lst.index('python'))  # ValueError
print(lst.index(98, 1, 3))  # 从索引为1的地方开始查找 查找到索引3 但不包括3
'''

'''
# 获取列表的单个元素
lst = ['hello', 'world', 98, 'hello', 'python', 234]
# 获取索引为2的元素
print(lst[2])
# 逆向索引
print(lst[-3])  # hello

# 获取列表的多个元素
# 切片
# 语法---> 序列[开始位置下表:结束位置下表:步长]
str1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(str1[2:5])  # [2, 3, 4]  步长不写默认1
print(str1[2:5:1])  # [2, 3, 4]
print(str1[2:5:2])  # [2, 4]
print(str1[:5])  # [0, 1, 2, 3, 4] 开始不写默认0
print(str1[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  开始结束都不写打印全部 开始默认0 结束默认结尾 步长默认1
print(str1[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  步长写负数倒序打印
print(str1[-4:-1])  # [6, 7, 8]  下表为负数 -1表示最后一个数据 一次再向前类推 打印时不包含-1的位置
# 如果选取方向和步长方向冲突 则无法选取数据
# print(str1[-4:-1:-1])  # 不能选取数据 从-4开始到-1结束 选取方向从左到右 但是步长为-1 方向从右到左
print(str1[-1:-4:-1])  # [9, 8, 7]
'''

'''
# 列表元素的判断及遍历
print('p' in 'python')
print('k' not in 'python')

lst = [10, 20, 'python', 'hello']
print(10 in lst)  # True
print('hello' not in lst)  # False

# 遍历
for item in lst:
    print(item)
'''

# 列表的增 删 改 查
'''
# 向列表的末尾添加
lst = [10, 20, 30]
print('添加元素之前', lst, id(lst))
lst.append(100)  # 末尾添加一个元素
print('添加元素之后', lst, id(lst))

lst2 = ['hello', 'world']
# lst.append(lst2)  # 将lit2作为一个元素添加到末尾
# print(lst)  # [10, 20, 30, 100, ['hello', 'world']]
lst.extend(lst2)  # 在列表末尾添加多个元素
print(lst)  # [10, 20, 30, 100, 'hello', 'world']

lst3 = [10, 20, 30]
lst3.insert(1, 90)  # 在列表任意位置添加
print(lst3)  # [10, 90, 20, 30]

lst4 = [True, False, 'hello']
# 在任意位置添加N个元素
# 切片
lst4[1:] = lst3
print(lst4)  # [True, 10, 90, 20, 30]
'''

'''
# 删除列表中的一个元素
lst = [10, 20, 30, 40, 50, 30]
lst.remove(30)
print(lst)  # [10, 20, 40, 50, 30]

lst2 = [10, 20, 30, 40, 50, 30]
# pop()根据索引移除元素
lst2.pop(1)
print(lst2)  # [10, 30, 40, 50, 30]
lst2.pop()  # 不指定索引 删除列表最后一个元素
print(lst2)  # [10, 30, 40, 50]

# 切片 删除至少一个元素 将产生一个新的列表对象
lst3 = [10, 20, 30, 40, 60, 50]
new_list = lst[1:3]
print('切片前', lst3)
print('切片后', new_list)

lst4 = [10, 20, 30, 40, 60, 50]
lst4[1:3] = []
print(lst4)  # [10, 40, 60, 50]

lst4.clear()
print(lst4)

del lst4
# print(lst4)  # NameError: name 'lst4' is not defined
'''

'''
# 修改列表中的值
lst0 = [10, 20, 30, 40]
print('修改前:', lst0)  # [10, 20, 30, 40]
# 修改一个值
lst0[2] = 100
print('修改后:', lst0)  # [10, 20, 100, 40]

lst1 = [10, 30, 60, 80]
lst1[1:3] = [300, 400, 500, 600]
print(lst1)  # [10, 300, 400, 500, 600, 80]
'''

'''
# 列表元素排序
lst0 = [20, 40, 10, 12, 64]
print('排序前:', lst0, id(lst0))
lst0.sort()  # 默认升序
print('排序后:', lst0, id(lst0))  # 内存地址一样 是在原列表排序的 没有开辟新地址
lst0.sort(reverse=True)  # 降序排序
print(lst0)
'''

# 列表生成式
lst0 = [i for i in range(1, 10)]
print(lst0)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = [i * i for i in range(1, 10)]
print(lst1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
lst2 = [i * 2 for i in range(1, 6)]
print(lst2)  # # [2, 4, 6, 8, 10]
