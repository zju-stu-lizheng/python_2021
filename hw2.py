def find_odd(li):
    '''
    找出传入的列表或元组的奇数位对应的元素
    :param args: 列表或元组
    :return: 返回新的列表
    '''
    li_new = []
    i = 0
    for item in li:
        if(i % 2 == 1):
            li_new.append(item)
            pass
        i += 1
        pass
    return li_new


print(find_odd([23,45,23,45,66]))