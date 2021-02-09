'''
使用私有属性的场景
1.把特定的一个属性隐藏起来，不想让类的外部直接调用
2.我想保护这个属性 不想让属性的值随意的改变
3.保护这个属性 不想让派生类【子类】去继承
'''


class Person:
    __hobby = '跳舞'  # 私有的类属性
    def __init__(self):
        self.__name = '李四'  # 加两个下划线，将此属性私有化 就不能在外部直接访问了
        self.age = 30
        pass

    def __str__(self):
        '''
        私有化的属性在内部可以使用self.__name
        :return:
        '''
        return '{}的年龄是{} 爱好是{}'.format(self.__name,self.age,self.__hobby)

    def changeValue(self):
        Person.__hobby = '唱歌'
    pass


class Student(Person):
    def printInfo(self):
        print(self.__name)  # 在此访问父类中的私有属性 可以吗？
    pass


xl = Person()
# print(xl.name)
print(xl)
stu = Student()

# print(Person.__hobby)
# stu.printInfo()
print(stu.age)
# print(stu.name)
print(stu)
print('---改变属性---')
stu.changeValue()
print(stu)

'''
1.私有化的【实例】属性 不能在外部直接的访问 可以在类的内部随意的使用
2.子类不能继承父类的私有化属性【只能继承公共的】
3.在属性名前面直接加’__‘，可以变为私有化属性
'''


