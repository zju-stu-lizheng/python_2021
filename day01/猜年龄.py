#猜年龄小游戏
print('请猜猜我的年龄')
age = 19
while True:
    i = 0
    flag = 0
    while i < 3:
        caice = eval(input())
        i+=1
        if(caice == age):
            print('猜对了')
            flag = 1
            break
        else:
            print('猜错了')
    if(flag == 1):
        break
    info = input('输入Y继续游戏，输入N结束游戏\n')
    if(info == 'N'):
        break
