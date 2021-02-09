# 动态添加方法
import types  # 添加方法的库


# 定义一个方法
def dymicMethod(self):
    print('{}的专业是{}，在{}'.format(self.name,self.pro,self.school))
    pass


@classmethod
def classTest(cls):
    print('这是一个类方法')
    pass

@staticmethod
def staticMethodTest():
    print('这是一个静态方法')
    pass


class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass
    def __str__(self):
        return '{}今天{}岁了'.format(self.name,self.age)
    pass

print('---------------绑定类方法---------------')
Student.TestMethod = classTest
Student.TestMethod()
Student.TestStaticMethod = staticMethodTest
Student.TestStaticMethod()

print('---------------给类对象添加属性---------------')
# 给类对象添加属性
Student.school = '浙江大学'
zyh = Student('张艳华',20)
zyh.pro = '计算机'  # 动态添加类属性
print(zyh,zyh.pro)

print('---------------动态添加方法---------------')
zyh.printInfo = types.MethodType(dymicMethod,zyh)  # 动态的绑定方法
zyh.printInfo()

print('---------实例对象调用 动态绑定类方法---------')
zyh.TestMethod()

print('---------------另一个实例对象---------------')
zm = Student('张敏',20)
print(zm)
# print(zm.weight)
print(zm.school)
