'''
什么是函数：一系列python语句的组合
一般是完成具体的独立的功能
为什么要使用函数：
代码的复用最大化以及最小化冗余代码
函数定义
def + 关键字 + 小括号 + 冒号 + 换行缩进 + 代码块
def 函数名 ():
    代码块
函数调用
本质上就是去执行函数定义里面的代码块，再调用函数之前，必须先定义
'''


# 函数的定义
def printInfo(name,height,weight,hobby,profess):
    '''
    这个函数是用来打印个人信息的，是对小张信息的打印
    :return:
    '''
    # 函数代码块
    print('%s的身高是%f' % (name,height))
    print('%s的体重是%f' % (name, weight))
    print('%s的爱好是%s' % (name,hobby))
    print('%s的专业是%s' % (name,profess))
    pass


# 函数的调用
printInfo('小张',1.7, 160, '唱歌', '计算机信息管理')
# 处理其他的逻辑信息
# 多次去打印出小航的信息
