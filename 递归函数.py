'''
什么是递归函数？
自己调用自己，必须有一个明确的结束条件
优点：逻辑简单，定义简单
缺点：容易导致栈溢出
'''

# 求阶乘
def fact(n):
    result = 1
    for item in range(1,n+1):
        result *= item
        pass
    return result


def fact_rec(n):
    '''
    递归实现
    :param n:
    :return:
    '''
    if n == 1:
        return 1
    else:
        return n*fact_rec(n-1)
    pass


# print(fact_rec(5))

import os   #文件操作模块


# 递归案例 模拟实现 树形结构的遍历
def findFile(file_Path):
    listRs = os.listdir(file_Path)  #得到该路径下所用的所有的文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_Path,fileItem)    # 组合完整文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            findFile(full_path)  # 如果是一个文件夹 再次递归
            pass
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass


# 调用搜索
findFile('C:\\Users\\1\\Desktop\\vscode\\python\\fishc')

