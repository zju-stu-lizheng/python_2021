'''
try...except语句
1.将可能出错的代码放到try里面，except可以捕获类型错误
2.except 在捕获错误异常时，只能根据具体的错误类型来捕获
3.用一个块可以捕获多个不同类型的异常
4.Exception 可以捕获所有的异常 当对出现的问题不确定时
可以使用exception
'''
import exception
try:
    # print(b)    # 捕获逻辑的代码
    # li = [1, 2, 34]
    # print(li[10])  # 通过下标去访问列表
    a = 10/0
    pass
# except NameError as msg:
#     # 捕获到的错误 才会在这里执行
#     print(msg)
#     pass
# except IndexError as msg:
#     # 捕获到的错误 才会在这里执行
#     print(msg)
#     pass
except Exception as result:
    print(result)
print('初次接触异常处理')
print('HAHAHAHA')


def A(s):
    return 10/int(s)
    pass

def B(s):
    return A(s)*2

def main():
    try:
        B('0')
        pass
    except Exception as msg:
        print(msg)
    pass


# main()
# 不需要在每个出错的地方去捕获，只要在合适的层次去捕获错误就可以了
# 就大大减少我们写try--except的麻烦
'''
异常的抛出机制
如果在运行时发生异常 解释器会查找相应的异常捕获类型
如果在当前函数里面没有找到的话，他会将异常传递给上层的调用函数，看能否处理
如果在最外层 没有找到的话 解释器就会退出程序 down
'''

# try-except-else
try:
    # print(aa)
    pass
except Exception as msg:
    print(msg)
    pass
else:
    print('当前面没有捕获到错误时')
    pass

# try-except-finally
try:
    # print(aa)
    pass
except Exception as msg:
    print(msg)
    pass
finally:
    print('不管有没有出错都执行的代码块')
    pass

