'''
在python中展现面向对象的三大特征
封装、继承、多态
封装：指的是把内容封装到个地方，便于后面的使用
需要：
把内容封装到某个地方
从另一个地方去调用被封装的内容

对于封装来说 其实就是使用初始化构造方法将内容封装到对象中,然后通过对象直接
或者self间接的获取被封装的内容

继承：和现实生活当中的继承是一样的：也就是 子可以继承父的内容
【属性和行为】（爸爸有的儿子都有，相反 儿子有的 爸爸不一定有）
'''


class Animal(object):
    def eat(self):
        '''
        吃
        :return:
        '''
        print('吃饭了')
        pass
    def drink(self):
        '''
        喝
        :return:
        '''
        print('喝水了')
        pass
    pass


# 继承Animal父类 此时Dog就是子类
class Dog(Animal):
    def wwj(self):
        '''
        子类独有的实现
        :return:
        '''
        print('小狗汪汪叫')
    pass


class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')
    pass


d1 = Dog()
d1.eat()    # 具备了吃的行为
d1.wwj()

'''
继承，可以极大的提高效率 减少代码的重复编写，精简代码的层级结构
'''




