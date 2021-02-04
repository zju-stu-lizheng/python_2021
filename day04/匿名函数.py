'''
匿名函数
语法：
lambda 参数1、参数2...:执行表达式
特点：
1.使用lambda关键字去创建函数
2.没有名字的函数
3.冒号后面的表达式有且只有一个
4.匿名函数自带return，而这个return的结果就是表达式计算后的结果
'''
def computer(x,y):
    '''
    计算数据累加和
    :param x:
    :param y:
    :return:
    '''
    return x+y
    pass


# print(computer(10,45))
# 通过变量去调用匿名函数
M = lambda x,y:x+y
print(M(23,19))








