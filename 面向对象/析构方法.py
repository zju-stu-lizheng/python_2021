class Animal:
    def __init__(self,name):
        self.name = name
        print('这是构造初始化方法')
        pass

    def __del__(self):
        '''
        用于资源回收，利用该方法销毁对象回收内存等资源
        :return:
        '''
        print('当在某个作用域下面，没有被使用【引用】的情况下 解析器会自动的调用此函数'
              '来释放内存空间')
        print('这是析构方法')
        print('%s 这个对象 被彻底清理了' % self.name)
        pass

    pass


cat = Animal('cat')
# print('内部')
del cat
input('程序等待中....')
# dog = Animal('柯基小狗')








