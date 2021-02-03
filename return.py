# 函数返回值
# 概念：函数执行完以后会返回一个对象，如果在函数的内部有return 就可以返回实际的值，否则返回None
# 类型，可以返回任意类型，返回值类型应该取决于return后面的类型
# 用途：给调用方返回数据
# 如果在一个函数体内执行了return，就意味着函数就退出了，return 后面的语句将不会执行
def Sum(a,b):
    sum = a + b
    return sum


# rs = Sum(10,30)  # 将返回值赋给其他的变量
# print(rs)   # 函数的返回值返回到调用的地方


def calComputer(num):
    li = []
    result = 0
    i = 1
    while i <= num:
        result += i
        i += 1
        pass
    li.append(result)
    return li
    pass


# rs = calComputer(10)
# print(type(rs))
# print(rs)


def returnTuple():
    '''
    返回元组类型的数据
    :return:
    '''
    return 1, 2, 3


A = returnTuple()
print(type(A))
print(A)









