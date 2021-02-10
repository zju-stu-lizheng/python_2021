# tell 返回指针当前所在的位置
# utf-8 一个汉字占用三个字符
# with open('Test.txt','w') as f:
#     for i in range(10):
#         f.write('')
#     pass

# with open('Test.txt','r',encoding='utf-8') as f:
#     print(f.read(3))
#     print(f.tell())
#     pass

# fobjB = open('Test.txt','r',encoding='utf-8')
# print(fobjB.read())
# fobjB.close()
# print('截取之后的数据......')
#
# fobjA = open('Test.txt',
#              'r+',
#              encoding='utf-8')
# fobjA.truncate(15)
# print(fobjA.read())
# fobjA.close()

# seek 控制光标所在位置
with open('Test_备份_.txt', 'rb') as f:
    data = f.read(2)
    print(data.decode('gbk'))
    print(f.tell())
    f.seek(-2, 1)  # 相当于光标又设置到了0的位置
    data = f.read(4)
    print(data.decode('gbk'))
    print(f.tell())
    f.seek(-6, 2)  # 光标在末尾处 往回移动了6个字符
    data = f.read(6)
    print(data.decode('gbk'))
    print(f.tell())
    f.seek(2, 0)    # 光标从0位置往右移动2字符
    data = f.read(6)
    print(data.decode('gbk'))
    print(f.tell())

'''
用 r 模式打开文件，在文本文件中，没有使用二进制的选项打开文件，
[只允许]从文件开头计算位置
'''