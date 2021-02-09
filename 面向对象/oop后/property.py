'''
实现方法
1.property
2.装饰器
'''
class Person:
    def __init__(self):
        self.__age = 18     # 定义一个私有化属性，属性名之前加__
        pass

    # def get_age(self):      # 访问私有实例属性
    #     return self.__age
    #
    # def set_age(self,age):  # 修改私有实例属性
    #     if age < 0:
    #         print('年龄不能小于0')
    #         pass
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    # # 定义一个类属性 实现通过直接访问属性的形式去访问私有属性
    # age = property(get_age,set_age)
    # 实现方法二 通过装饰器的方式去声明
    @property  # 用装饰器修饰 添加属性标识 提供一个getter方法
    def age(self):
        return self.__age

    @age.setter  # 使用装饰器进行修饰 提供一个setter方法
    def age(self,age):
        if age < 0:
            print('年龄不能小于0')
            pass
        else:
            self.__age = age
            pass
        pass

    pass


p1 = Person()
# p1.age = 10
# p1.set_age(10)
# print(p1.get_age())

p1.age = 25
print(p1.age)
p1.age = -1
print(p1.age)