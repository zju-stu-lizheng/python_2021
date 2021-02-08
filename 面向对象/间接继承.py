class GranFather:
    def eat(self):
        print('吃的 方法')
        pass
    pass

class Father(GranFather):
    pass

class Son(Father):
    pass

son = Son()
print(Son.mro())
son.eat()   # 此方法是从GranFather继承过来的
