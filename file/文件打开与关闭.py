# 文件的操作
# 打开文件 open
# 默认的编码是gbk 这个是中文编码 最好的习惯就是我们在打开一个文件时
# 给它指定一个编码类型
# fobj = open('./Test.txt','w+',encoding='utf-8')
# # 开始操作 读/写操作
# fobj.write('在苍茫的大海上')
# fobj.write('狂风卷积着乌云')
# fobj.close()

# 以二进制形式写入
# fobj = open('Test.txt','wb')  # str-->bytes
# fobj.write('在乌云和大海之间'.encode('utf-8'))
# fobj.close()
# fobj = open('Test.txt','wb')
# fobj.write('在乌云和大海之间\r\n'.encode('utf-8'))
# fobj.write('海燕像黑色的闪电\r\n'.encode('utf-8'))
# fobj.close()

# f = open('Test.txt','r',encoding='utf-8')
# # print(f.read())
# print(f.readlines())

# f = open('Test.txt','rb')
# data = f.read()
# print(data)
# print(data.decode('utf-8'))     # 读取所有的数据
# f.close()

# with上下文管理
with open('Test.txt','a',encoding='utf-8') as f:
    # print(f.read())
    f.write('我觉得python非常的好学\n')
    pass

'''
小结
文件读写的几种操作方式
[read]    r r+ rb rb+ 
r r+ 只读  适用普通读取场景
rb rb+ 适用于文件 图片 视频 音频这样文件读取

[write]   w w+ wb+ wb a ab
        w wb+ w+:每次都会去创建文件
        二进制读写要注意编码问题，默认写入文件的编码是gbk
        
【append】 a ab a+
        追加，在【文件指针的末尾】去追加，并不会每次都去创建一个新的文件
'''

