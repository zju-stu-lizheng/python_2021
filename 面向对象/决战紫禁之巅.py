'''
问题分析：
1.决战紫禁之巅有两个任务，西门吹雪以及叶孤城
    （1）属性：
    name：玩家名字
    blood：玩家血量
    （2）方法：
    tong：捅对方一刀，对方掉血10滴
    kanren：砍对方一刀，对方掉血15滴
    chiyao：吃一颗药，补血10滴
    __str__打印玩家状态
'''
import time  #导入时间库
import random


# 第一步 需要先去定义一个类【角色类】
class Role:
    def __init__(self,name,hp):
        '''
        构造初始化函数
        :param name:角色名
        :param hp: 血量
        '''
        self.name = name
        self.hp = hp
        pass

    def __str__(self):
        return '%s 剩余血量为 %d' % (self.name,self.hp)

    def tong(self,enemy):
        '''
        捅一刀
        :param enemy:敌人
        :return:
        '''
        enemy.hp -= 10
        info = '[%s] 捅了[%s] 一刀'% (self.name,enemy.name)
        print(info)
        pass

    def kanren(self,enemy):
        '''
        砍人
        :param enemy:敌人
        :return:
        '''
        enemy.hp -= 15
        info = '[%s] 砍了[%s] 一刀' % (self.name, enemy.name)
        print(info)
        pass

    def chiyao(self):
        '''
        吃药
        :return:
        '''
        if self.hp <= 90:
            self.hp += 10
            info = '[%s] 吃了一颗补血药，增加血量10点' % self.name
            pass
        else:
            info = '[%s] 吃了一颗补血药，血量已满' % self.name
        print(info)
        pass

    pass


# 创建2个【西门吹虚、叶孤城】实例化对象
xmc = Role('西门吹雪', 100)
ygc = Role('叶孤城', 100)

seed = input('请输入一个数字：表示不同平行世界的对战\n')
random.seed(seed)

while True:
    if xmc.hp <= 0 or ygc.hp <= 0:
        # 满足条件， 推出循环
        break
        pass

    ran = random.random()
    # print(ran)
    if ran < 1.0/6:
        xmc.tong(ygc)  # 西门吹雪捅叶孤城一刀
        print(xmc)  # 打印对象状态
        print(ygc)
        print('********************')
        pass
    elif ran < 2.0/6:
        ygc.kanren(xmc)  # 西门吹雪捅叶孤城一刀
        print(xmc)  # 打印对象状态
        print(ygc)
        print('********************')
    elif ran < 3.0/6:
        xmc.kanren(ygc)  # 西门吹雪捅叶孤城一刀
        print(xmc)  # 打印对象状态
        print(ygc)
        print('********************')
    elif ran < 4.0/6:
        ygc.tong(xmc)  # 西门吹雪捅叶孤城一刀
        print(xmc)  # 打印对象状态
        print(ygc)
        print('********************')
    elif ran < 5.0/6:
        xmc.chiyao()  # 西门吹雪捅叶孤城一刀
        print(xmc)  # 打印对象状态
        print(ygc)
        print('********************')
        pass
    else :
        ygc.chiyao()  # 西门吹雪捅叶孤城一刀
        print(xmc)  # 打印对象状态
        print(ygc)
        print('********************')
        pass
    time.sleep(1)  # 休眠1s
    pass

print('对战结束')





