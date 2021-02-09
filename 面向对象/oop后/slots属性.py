'''
slot作用：
限制我们要添加的实例属性
节约内存资源
'''
class Student(object):
    __slots__ = ('name', 'age', 'score')  # 取消__dict__魔术方法
    def __str__(self):
        return '{}....{}'.format(self.name,self.age)
    pass


xw = Student()
xw.name = '校网'
xw.age = 20
xw.score = 96
# print(xw.__dict__)  # 所有可以用属性都在这里储存  不足的地方就是占用的内存空间大
# 可以看到 在定义了 slots变量之后 student类的实例已经不能随意创建
# 溶蚀还可以看到实例中也不存在__dict__
print(xw)

# 在继承关系当中的使用 __Slots__
# 子类未申明 __slots__时，那么不会继承父类的__slots__,此时子类可以随意的属性赋值
# 子类申明了__slots__时，继承父类的__slots__，也就是子类__slots__的范围是
# 其自身+父类的
class subStudent(Student):
    __slots__ = ('gender')
    pass

ln = subStudent()
ln.score = 87
ln.name = 'ln'
ln.age = 20
ln.gender = '男'
print(ln.gender)    # 可以显示
print(ln)







