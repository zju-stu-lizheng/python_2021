def modified_dict(di):
    '''
    检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容
    返回给调用者
    :param args: 字典
    :return: 返回新的字典
    '''
    dict_new = {}
    for key, value in di.items():
        if len(value) > 2:
            dict_new[key] = value[0:2]
            pass
        else :
            dict_new[key] = value
            pass
        pass
    return dict_new


print(modified_dict({"age": '35', "name": "peter", "专业":"计算机科学与技术"}))
