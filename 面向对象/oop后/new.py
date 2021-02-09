'''
new方法，创建并返回一个实例对象，如果__new__只调用一次，就会得到
一个对象
'''


class Animal(object):
    def __init__(self):
        self.color = 'red'
        pass

    # 在python中 如果不重写  __new__默认结构如下
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)  # 不能调用自己，否则无限递归
    pass

tigger = Animal()  # 实例化的过程，自动调用 new去创建实例

# 在新式类中 __new__才是真正的实例化方法，为类提供外壳制造出实例框架
# 然后调用该框架内的构造方法 __init__进行丰满操作
# 比喻建房子 __new__方法负责开发地皮，打地基 并将原料存放在工地，
# 而__init方法负责从工地取材料建造出地皮开发图纸规定的大楼
# 负责设计、建造细节


