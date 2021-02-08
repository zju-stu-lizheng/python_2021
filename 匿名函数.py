'''
匿名函数
语法：
lambda 参数1、参数2...:执行表达式
特点：
1.使用lambda关键字去创建函数
2.没有名字的函数
3.冒号后面的表达式有且只有一个
4.匿名函数自带return，而这个return的结果就是表达式计算后的结果
缺点
lambda 只能是单个表达式，不是一个代码块，lambda的设计就是为了满足简单函数的场景
仅仅封装有限的逻辑，复杂逻辑实现不了
'''
# def computer(x,y):
#     '''
#     计算数据累加和
#     :param x:
#     :param y:
#     :return:
#     '''
#     return x+y
#     pass


# print(computer(10,45))
# 通过变量去调用匿名函数
M = lambda x,y:x+y
# print(M(23,19))

result = lambda a,b,c:a*b*c
# print(result(12,34,2))

# age = 25
# print('可以参军' if age>18 else '继续上学')
#
# funcTest = lambda x,y:x if x>y else y
# print(funcTest(12,2))

rs = (lambda x,y:x if x>y else y)(16,12)    # 直接调用
print(rs)


varRs = lambda x:(x**2)+890
print(varRs(10))





