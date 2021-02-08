'''
多态：顾名思义就是多种状态、形态，就是同一种行为 对于不同的子类【对象】有
不同的行为表现

要想实现多态 必须得有两个前提需要遵守：
1.继承：多态必须发生在父类和子类之间
2.重写：子类需要重写父类的方法

多态的作用：
增加程序的灵活性
增加程序的扩展性
'''
# 案例演示
class Animal:
    '''
    父类[基类]
    '''
    def say_who(self):
        print('我是一个动物....')
        pass
    pass


class Duck(Animal):
    '''
    鸭子类【子类】【派生类】
    '''
    def say_who(self):
        print('我是一个鸭子')
        pass

    pass


class Dog(Animal):
    def say_who(self):
        print('我是一只小狗')
        pass
    pass


class Cat(Animal):
    def say_who(self):
        print('我是一只小猫')
        pass
    pass


class Bird(Animal):
    '''
    新增鸟类 无需修改原来的方法
    '''
    def say_who(self):
        print('I am a bird.')
        pass
    pass


def commonInvoke(obj):
    '''
    统一调用方法
    :param obj: 对象的实例
    :return:
    '''
    obj.say_who()
    pass


class People():
    pass


class Student(People):
    def say_who(self):
        print('我是一年级的学生 李敏')
        pass
    pass

# duck1 = Duck()
# duck1.say_who()
#
# dog1 = Dog()
# dog1.say_who()
#
# cat1 = Cat()
# cat1.say_who()

listObj = [Duck(),Dog(),Cat(),Bird(),Student()]
for item in listObj:
    '''
    循环去调用函数
    '''
    commonInvoke(item)
    pass
