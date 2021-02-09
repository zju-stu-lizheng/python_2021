'''
私有化方法，一般是类内部调用，子类不能继承，外部不能调用
'''


class Animal:
    def __eat(self):
        print('I eat')
        pass

    def run(self):
        self.__eat()  # 在此调用私有化的方法
        print('I run')
        pass
    pass

class Bird(Animal):
    pass

bird = Bird()
# bird.eat()
bird.run()