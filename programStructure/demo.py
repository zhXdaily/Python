# 顺序结构
print('--------程序开始--------')
print('1.把冰箱门打开')
print('2.把大象放冰箱里')
print('3.把冰箱门关上')
print('--------程序结束--------')

# 分支结构
# 对象的布尔值
# python中一切皆对象 所有对象都有一个布尔值
print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(None))  # False
print(bool(''))  # # False
print(bool([]))  # False 空列表
print(bool(list()))  # False 空列表
print(bool(()))  # False 空元组
print(bool({}))  # False 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合
print('---------以上对象的布尔值为False， 其他对象的布尔值均为True---------')
print(bool(18))  # True
print(bool('hello world'))  # True

# 分支结构 单分支结构-选择结构
