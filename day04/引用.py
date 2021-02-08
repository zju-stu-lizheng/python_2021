a = 1   # 给对象 1 贴上标签 a
# 不可变类型： 对同一变量赋值，内存存的数据不变，但是变量指向的地址变了
# int,tuple


def func(x):
    print('x的地址：{}'.format(id(x)))
    x = 2   # 修改之后，x对应的对象修改成了 2，而 2 的内存地址与 1 不同
    print('x的值修改后地址：{}'.format(id(x)))
    print('x的值修改后a的地址:{}'.format(id(a)))
    pass


# 调用函数
print('a的地址:{}'.format(id(a)))
func(a)     # 传递的是地址的引用

# 可变类型:地址不再改变，改变的是内存地址上存储的值
li = []


def testRenc(parms):
    print('li的地址{}'.format(id(parms)))
    li.extend([1,3,4,54,67])
    print('li修改后的地址{}'.format(id(parms)))
    pass


print(id(li))
testRenc(li)
print(li)


'''
小结：
1.在python中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用
2.了解了原理之后，就可以更好的去把控在函数内部的处理是否会影响到函数外部的变量变化
参数传递是通过对象引用来完成的
'''







