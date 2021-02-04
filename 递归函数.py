'''
什么是递归函数？

'''

# 求阶乘
def fact(n):
    result = 1
    for item in range(1,n+1):
        result *= item
        pass
    return result

print(fact(5))