# list:有序的数据集合
# 特点：
#  1.支持增删改查
#  2.列表中的数据实可以变化的
#  3.用[]来表示列表类型，数据项之间用逗号来分割，注意：数据项可以是任何类型的数据
#  4.支持索引和切片

"""
list = [1, 2, 3, "你好"]

strA = '我喜欢python'
print(len(strA))
list.append(strA)
print(len(list))
print(list)
"""

listA = ['abcd', 785, 12.23, 'qiuzhi', True]
'''
print(listA)    # 输出完整的列表
print(listA[0])     # 输出第一个元素
print(listA[1:])

print('--------append--------')
listA.append(['fff', 'ddd'])    #末尾添加（追加）
print(listA)
listA.insert(1,'这是我刚插入的数据')  # 在第二个数据位置
print(listA)

rsData = list(range(10))    # 强制类型转换
print(type(rsData))

listA.extend(rsData)    # 扩展：批量添加
print(listA)
'''


print("-----修改-------")
listA[0] = 333.6
print(listA)

listB = list(range(10, 50))
print('------delete data-----')
# print(listB)
# del listB[0]
# print(listB)
# del listB[1:3]  # 批量删除多项数据 slice
# print(listB)

# listB.remove(20)  # 移除指定的元素
listB.pop(1)    # 可以移除指定的项
print(listB)

print(listB.index(19))



