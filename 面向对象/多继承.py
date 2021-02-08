class shenxian:
    def fly(self):
        print("神仙都会飞")
        pass
    pass


class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')
        pass
    pass

class Sunwukong(shenxian,Monkey):
    pass

# 问题是：当多个父类当中存在相同方法的时候 应该去调用哪一个呢
class D(object):
    def eat(self):
        print('D.eat')
        pass
    pass


class C(D):
    # 方法覆盖
    def eat(self):
        print('C.eat')
        pass
    pass


class B(D):
    pass


class A(B,C):
    pass


a = A()
a.eat()  # 在执行eat的方法时，查找方法的顺序是【广度优先BFS】
print(A.__mro__)    # 可以显示类的依次继承关系
# 首先到A里面找，如果A无，去B；B无，去C；C无，去B的父类(D)找

# swk = Sunwukong()
# swk.chitao()
# swk.fly()





