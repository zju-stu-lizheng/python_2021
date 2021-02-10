class Person:
    # 定义一个python类，两个私有属性
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
        pass

    def __str__(self):
        return '{}的年龄是{}'.format(self.__name,self.__age)

    # 获取用户信息的函数
    def GetAgeInfo(self):
        return self.__age

    def GetNameInfo(self):
        return self.__name

    # 设置用户信息的函数
    def SetAgeInfo(self,age):
        if age > 0 and age < 120:
            self.__age = age
            pass
        else:
            print('您输入的数据不合法')
        pass

    def SetNameInfo(self, name):
        self.__name = name
        pass


'''
一个单例模式
'''
class DataBaseClass:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super.__new__(cls, *args, **kwargs)
            pass
        return cls._instance
    pass


class Student:
    def __init__(self):
        self.__name = '张三'
        self.__score = 90
        pass

    def __str__(self):
        return '{}的分数是:{}'.format(self.__name,self.__score)

    def __call__(self, *args, **kwargs):
        print(self.__name+'的得分是:'+str(self.__score))
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
        pass

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
        pass
    pass

xw = Student()
xw()    # 将实例对象咦函数的形式去调用
print(xw)


# 实例化一个cat对象，给cat对象动态绑定一个run方法
import types
def run(self):
    print('小猫快跑...')
    pass
def info():
    print('ok')
    pass

class Animal:
    pass

Animal.color = '黑色'  # 绑定类属性
Animal.info = info
cat = Animal()
cat.run = types.MethodType(run,cat)  # 动态绑定
print(cat.color)
Animal.info()
