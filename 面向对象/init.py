# class People:
#     def __init__(self):
#         self.name = '小倩'
#         self.sex = '女生'
#         self.age = 20
#         pass
#     def eat(self):
#         '''
#         吃的行为
#         :return:
#         '''
#         print('喜欢吃榴莲')
#         pass
#     pass
#
# xq = People()
# # 添加实例属性
# # xq.name = '小千'
# # xq.sex = '女生'
# # xq.age = 20
# print(xq.name,xq.sex,xq.age)    # 输出默认值
#
#
# xl = People()
# # 添加实例属性
# xl.name = '小立'
# xl.sex = '女生'
# xl.age = 20
# print(xl.name,xl.sex,xl.age)


# 改进
class People:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
        pass
    def eat(self,food):
        '''
        吃的行为
        :return:
        '''
        print(self.name+'喜欢吃'+food)
        pass
    pass

yp = People('yp', '男生', 18)
print(yp.name, yp.age, yp.sex)
yp.eat('香蕉')
cc = People('cc', '男生', 20)
print(cc.name, cc.age, cc.sex)
cc.eat('抽代')


# 总结 __init__
# 1.python自带的内置函数，具有特殊的函数  使用双下划线
# 包起来的【魔术方法】
# 2.是一个初始化的方法，用来定义实例属性 和初始化数据的 在创建对象
# 时自动调用
# 3.利用传参的机制可以让我们定义功能更加强大并且方便的类

