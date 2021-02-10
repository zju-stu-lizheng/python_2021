# 备份
def copyFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名:')
    file_list = old_file.split('.')
    # 构造新的文件名
    new_file = file_list[0]+'_备份_.'+file_list[1]
    old_f = open(old_file,'r',encoding='utf-8')  # 要打开需要备份的新文件
    new_f = open(new_file,'w')  # 以写的模式打开新文件
    content = old_f.read()  # 将文件内容读取出来
    new_f.write(content)    # 备份
    old_f.close()
    new_f.close()
    pass

# copyFile()

def copyBigFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名:')
    file_list = old_file.split('.')
    # 构造新的文件名
    new_file = file_list[0]+'_备份_.'+file_list[1]
    try:
        # 监视要处理的逻辑
        with open(old_file,'r',encoding='utf-8') as old_f,open(new_file,'w') as new_f:
            while True:
                content = old_f.read(1024)   # 一次性读取1024
                new_f.write(content)
                if len(content) < 1024:
                    break
                    pass
                pass
            pass
        pass
    except Exception as msg:
        print(msg)
        pass
    pass


copyBigFile()