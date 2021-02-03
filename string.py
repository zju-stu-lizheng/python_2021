# 序列: 在python中，序列就是一组按照顺序排列的值[数据集合]
# 切片是指截取字符串中的一段内容
# 三种序列类型:字符串、列表、元组
# 第一个正索引为0，指向左端，第一个索引为负数时，指向的是右端
"""
[起始下标:结束下标:步长] 不包含结束下标对应的数据，步长指的是隔几个下标获取
"""
# Test = 'python'
# # print(type(Test))
# print('获取第一个字符', Test[0], sep='')
# for i in Test:
#     print(i)
# name = 'peter'
# print('姓名首字母转换大写%s' % name.capitalize())
# a = '   hello    '
# b = a.strip()  # 去除空格
# print(a.rstrip())
# b = a
# print('a的内存地址',id(a))
# print('b的内存地址',id(b))
# dataStr = 'I love Python'
# print(dataStr.find('P'))    # find函数可以查找目标对象在序列对象中的值
# print(dataStr.index('o'))  # index 检测字符串是否包含子字符串,返回下标值
# print(dataStr.startswith('I'))
# print(dataStr.endswith('n'))
#
# print(dataStr.lower())
# print(dataStr.upper())

strMsg = 'hello world'
print(strMsg[2:5])
print(strMsg[2:])
print(strMsg[::3])
