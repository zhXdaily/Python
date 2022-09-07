"""元组"""


"""
'''可变序列 列表 字典  增删改后地址不变 '''
lst = [10, 20, 30]
print(id(lst))  # 2028785603392
lst.append(300)
print(id(lst))  # 2028785603392

'''不可变序列 元组 字符串 增删改后地址改变 因此没有增删改操作'''
s = 'hello'
print(id(s))  # 1933007073328
s = s + 'world'
print(id(s))  # 1933007421040
"""


"""
'''元组的创建'''
'''1、使用()'''
t = ('python', 'world', 98)  # 括号可以不写 t = 'python', 'world', 98
# 如果元组内只有一个元素要写成
tt = ('python', )

print(t)
print(type(t))

print(tt)
print(type(tt))

'''2、使用内置函数tuple'''
t1 = tuple(('python', 'world', 98))
print(t1)
print(type(t1))
"""


"""
t = (10, [20, 30], 40)
print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
"""


'''元组的遍历'''
t = ('python', 'world', 98)
print(t[0])
print(t[1])
print(t[2])

for item in t:
    print(item)