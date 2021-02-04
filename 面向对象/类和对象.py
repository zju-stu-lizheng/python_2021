'''
类相当于制造汽车的图纸，用这个图纸制造的汽车相当于对象
  是一组 相同或者相似特征【属性】和行为【方法】的一系列对象组合
类的组成部分:
1.类名
2.类的属性：一组数据
3.类的方法：允许对进行操作的方法（行为）

类是对象的抽象化，而对象是类的一个实例

#定义类和对象

    实例方法：在类的内部，使用def 关键字来定义 第一个参数默认是 self
    【名字标识可以是其它的名字，但是这个位置必须被占用】

    实例方法是归于 类的实例所有

    属性：在类的内部定义的变量【类属性】，定义在方法里面使用self
    应用的属性【实例属性】
'''


# 创建一个类
class Person:  # 大驼峰命名法
    '''
    对应人的特征
    '''
    # name = 'lz'     # 类属性
    age = 19        # 类属性
    '''
    对应人的行为  实例方法
    '''
    def __init__(self):
        self.name = '小明'    # 实例属性
    def eat(self):
        print("{}大口地吃饭".format(self.name))
        pass
    def moyu(self):
        print("{}悠哉地摸鱼".format(self.name))
        pass


# 创建一个对象[类的实例化]
# 规则格式 对象名=类名()
lizheng = Person()
lizheng.name = 'lizheng'
print('这个five的名字:{},年龄:{}'.format(lizheng.name,lizheng.age))
lizheng.eat()
lizheng.moyu()

# 创建另外一个实例对象
cc = Person()
cc.name = 'cc'
cc.eat()











