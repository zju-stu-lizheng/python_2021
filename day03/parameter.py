'''
参数的分类：
必选参数、默认参数【缺省参数】、可选参数、关键字参数
参数：其实就是函数为了实现某项特定的功能，进而为了得到实现功能所需要的数据
'''


# 1 必选参数
# def sum(a,b):  # 形式参数:只是意义上的一种参数，再定义的时候是不占内存地址的
#     sum = a+b
#     print(sum)
#     pass
#
#
# # 2 默认参数【缺省参数】
# def sum1(a=20,b=30):    # 缺省参数始终放在参数列表的尾部
#     print('默认参数使用=%d'%(a+b))
#     pass
#
#
# # 可变参数（当参数的个数不确定时使用，比较灵活
# def getComputer(*args):
#     '''
#     计算累加和
#     :param args: 可变长的参数类型
#     :return:
#     '''
#     # print(args)
#     result = 0
#     for item in args:
#         result += item
#         pass
#     print('result=%d'%result)
#     pass
#
#
# # 函数的调用
# sum(1,2)    # 1 2 实际参数：实参
# sum1()      # 在调用的时候，如果未赋值，就会用定义函数时给定的默认值
# getComputer(1)
# getComputer(1,2,3)

# 关键字可变参数
# **来定义
# 在函数体内 参数关键字是一个字典类型，key是一个字符串
def keyFunc(**kwargs):
    print(kwargs)
    pass

# 调用
dictA = {"name":'Leo', "age":35}
# keyFunc(**dictA)
# keyFunc(name='peter',age = 26)


# 组合的使用
def complexFunc(*args,**kwargs):
    print(args)
    print(kwargs)
    pass


complexFunc(1,2,3,4,name='刘德华')
complexFunc(age=36)


# def TestMup(**kwargs,*args):
#     '''
#     可选参数必须放到关键字可选参数之前
#     :param kwargs:
#     :param args:
#     :return: 
#     '''
#     pass





