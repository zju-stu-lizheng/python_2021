'''
__str__方法,__new__方法
'''

class Person:
    '''
    定义类
    '''
    def __init__(self,pro='计算机科学与技术',name='lz',food='榴莲'):
        '''

        :param pro: 专业
        :param name: 姓名
        :param food: 食物
        '''
        self.pro = pro
        self.name = name
        self.food = food
        print('---init---','函数执行')
        pass

    def __str__(self):
        '''
        打印对象 自定义对象 是内容格式的
        :return:
        '''
        return '%s喜欢吃%s 修的专业是%s'%(self.name,self.food,self.pro)
    
    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法，每调用一次，就会生成一个新的对象cls

        场景：
        可以控制创建对象的一些属性限定
        :param args: 
        :param kwargs: 
        '''
        print('---new---','函数的执行')
        return object.__new__(cls)  # 在这里是真正创建对象实例的
        pass

    def eat(self):
        '''
        实例方法
        :return:
        '''
        print('%s喜欢吃%s 修的专业是%s'%(self.name,self.food,self.pro))
        pass
    pass

xw = Person()
print(xw)


'''
__new__和__init__函数的区别
__new__是类的实例化方法，必须返回该实例，否则对象创建不成功
__init__是类的数据属性初始化方法，也可以认为是实例的构造方法，接受类的实例，self对其进行构造
__new__必须有cls参数，代表要实例化的类，此参数在实例化时由python解释器自动提供
__new__执行早于__init__
'''


