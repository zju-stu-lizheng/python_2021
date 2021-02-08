class People:
    country = 'china'

    @classmethod  # 类方法 用@classmethod来进行修饰
    def get_country(cls):
        return cls.country  # 访问类属性
        pass

    @classmethod
    def change_country(cls,data):
        cls.country = data  # 修改类属性的值，在类方法中
        pass

    @staticmethod
    def getData():
        return People.country

    @staticmethod
    def add(x,y):
        return x+y

    pass


print(People.getData())
print(People.add(10, 34))

# print(People.country)
# print(People.get_country())  # 通过类对象去引用
p = People()
print(p.getData())  # 注意一般情况下 不会通过实例对象去访问静态方法
# print('实例对象访问 %s'%p.country)
# print('-----------修改之后-------------')
# People.change_country('England')
# print(People.get_country())

'''
为什么要使用静态方法呢？
由于静态方法主要用来存放逻辑性的代码，本身和类以及实例对象没有交互，也就是说
在静态方法中，不会涉及到类中方法和属性的操作，
数据资源能够得到有效地利用
'''

# demo 返回当前的系统时间
import time     # 引入时间模块

class TimeTest:
    def __init__(self,hour,min,second):
        self.hour = hour
        self.min = min
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
        pass
    pass


print(TimeTest.showTime())

'''
从方法定义的形式可以看出来
1.类方法的第一个参数时类对象 cls 进而去引用类对象的属性和方法
@classmethod 来修饰
2.实例方法的第一个参数必须是self 通过这个self可以去引用类属性或者实例属性
若存在相同名称实例属性和类属性的话，实例属性的优先级最高
3.静态方法不需要定义额外的参数，若是要应用属性的话 则可以通过类对象
或者是实例对象去引用即可,必须用装饰器 @staticmethod 来修饰
'''