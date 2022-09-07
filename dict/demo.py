"""字典"""
'''每一个键值对不可以增删'''

"""
'''字典的创建'''
'''1、花括号{}'''
scores = {'张三': 100, '李四': 98, '王五': 97}
print(scores)
print(type(scores))  # <class 'dict'>

'''2、使用内置函数dict'''
stu = dict(name='jack', age=20)
print(stu)
print(type(stu))
"""


"""
'''字典中元素的获取'''
scores = {'张三': 100, '李四': 98, '王五': 97}
'''1、[]'''
print(scores['张三'])  # 100
# print(scores['陈六'])  # 报错 KeyError: '陈六'

'''2、get()'''
print(scores.get('张三'))  # 100
print(scores.get('陈六'))  # 不报错 输出None
print(scores.get('麻七', 99))  # 99  99是在查找麻七所对应value不存在时，提供的一个默认值
"""


"""
'''key的判断'''
scores = {'张三': 100, '李四': 98, '王五': 97}
print('张三' not in scores)  # False
print('张三' in scores)  # True

del scores['张三']
print(scores)  # {'李四': 98, '王五': 97}
# scores.clear()  # 清空字典元素
# print(scores)  # {}
scores['陈六'] = 98  # 新增元素
print(scores)  # {'李四': 98, '王五': 97, '陈六': 98}
scores['陈六'] = 50
print(scores)  # {'李四': 98, '王五': 97, '陈六': 50}
"""


"""
'''字典的视图操作'''
'''获取所有的key'''
scores = {'张三': 100, '李四': 98, '王五': 97}
keys = scores.keys()
print(keys)  # dict_keys(['张三', '李四', '王五'])
print(type(keys))  # <class 'dict_keys'>
# 将所有的key组成的视图转成列表
print(list(keys))  # ['张三', '李四', '王五']

'''获取所有的value'''
values = scores.values()
print(values)  # dict_values([100, 98, 97])
print(type(values))  # <class 'dict_values'>
print(list(values))  # [100, 98, 97]

'''获取所有的键值对'''
items = scores.items()
print(items)  # dict_items([('张三', 100), ('李四', 98), ('王五', 97)])
print(list(items))  # [('张三', 100), ('李四', 98), ('王五', 97)]
print(type(items))  # <class 'dict_items'>
"""


"""
'''字典元素的遍历'''
scores = {'张三': 100, '李四': 98, '王五': 97}
for item in scores:
    print(item, scores[item], scores.get(item))
"""


"""
'''字典的特点'''
d = {'name': '张三', 'name': '李四'}  # key不允许重复 value可以重复
print(d)  # {'name': '李四'}
"""


'''字典生成式'''
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)  # {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}
