# class GranFather:
#     def eat(self):
#         print('吃的 方法')
#         pass
#     pass
#
#
# class Father(GranFather):
#     def eat(self):  # 因为父类中已经存在这个的方法，在这里相当于 方法重写 【方法覆盖了】
#         print('爸爸经常吃海鲜')
#     pass
#
# class Son(Father):
#     pass
#
# son = Son()
# print(Son.mro())
# son.eat()   # 此方法是从GranFather继承过来的


'''
所谓重写，就是子类中有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法
为什么要重写，父类的方法已经不满足子类的需要，那么子类可以重写父类
'''
class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        pass

    def bark(self):
        print("汪汪叫....")
        pass
    pass

class kejiquan(Dog):
    def __init__(self,name,color):  # 属于重写父类的方法
        # 针对这种需求 我们需要去调用父类的函数
        # Dog.__init__(self,name,color)   # 手动调用 调用父类的方法
        super().__init__(name,color)    # 自动找到父类 进而调用方法
        # 假设继承了多个父类，那么会按照顺序逐个去找 然后再调用

        # 扩展其它属性
        self.height = 90
        self.weight = 20
        pass

    def __str__(self):
        return '{}的颜色是{} 它的身高是{}cm 体重是{}'.format(self.name,self.color,self.height,self.weight)

    def bark(self):
        super().bark()  # 调用父类的方法
        print('叫的和神一样')  # 属于重写类的方法
        # print(self.name)   # 没有这个属性，因为不再调用父类中的init
        pass
    pass

kj = kejiquan('柯基','黄色')
kj.bark()
print(kj)