'''
自定义异常：直接或间接继承Exception类
'''


class ToolongMyException(Exception):
    def __init__(self, long):
        '''

        :param long:长度
        '''
        self.len = long
        pass

    def __str__(self):
        return '您输入的姓名数据长度是' + str(self.len) + '已经超过长度'

    pass


def name_Test():
    name = input('请输入姓名...')
    try:
        if len(name) > 4:
            raise ToolongMyException(len(name))
        else:
            print(name)
    except ToolongMyException as result:
        print(result)
        pass
    finally:
        print('执行完毕了...')
    pass


name_Test()
