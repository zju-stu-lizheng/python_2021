'''
字典可以存储任意对象，由 键值对 组成的集合，通常使用 键 来访问数据
效率非常高，和list一样，支持对数据的添加、修改、删除

特点：
1.不是序列类型，没有下标的概念，是一个无序的 键值集合，是内置的高级数据类型
2.用{}来表示字典对象，每个键值对用逗号分隔
3.键 必须是不可变的类型【元组、字符串】 值可以是任意类型
4.每个键必定是唯一的，存在重复键会覆盖
'''
# 创建
dictA = {"pro":'艺术', 'school':'北京电影学院'}
# 添加
dictA['name'] = '李易峰'
dictA['age'] = '30'
dictA['pos'] = '歌手'
print(dictA)
print(len(dictA))

print(dictA['name'])  #通过键值获取对应的值
dictA['name'] = '谢霆锋'

print(dictA)

'''
# 获取所有的键
print(dictA.keys())
# 获取所有的值
print(dictA.values())
# 获取所有的键值对
print(dictA.items())
'''


for key, value in dictA.items():
    print('%s == %s'%(key, value))

# 更新，也可以添加
# dictA.update(({'age':32}))
# print(dictA)
# dictA.update(({'height':1.80}))
# print(dictA)

# 删除操作
# del dictA['name']
# dictA.pop('age')
print(dictA)

# 如何排序
# 按照key排序
print(sorted(dictA.items(), key=lambda d:d[0]))
# 按照value排序
print(sorted(dictA.items(), key=lambda d:d[1]))

