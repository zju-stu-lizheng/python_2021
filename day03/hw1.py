def sum_of_n(*args):
    '''
    接受n个数字，求这些参数数字的和
    :param args: n个数字
    :return: 和
    '''
    result = 0
    for i in args:
        result += i
        pass
    return result


print(sum_of_n(99,98,78))
