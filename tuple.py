'''
元组是一种不可变的序列，在创建之后不能做任何的修改
1.不可变
2.用（）来创建，数据项用逗号分隔
3.可以实任何的类型
4.当元组中只有一个元素是，要加上逗号，否则会被当做整形来处理
5.可以支持切片
'''

# 元组的创建 ,不能进行修改
# tupleA = ()
tupleA = ('abcd', 89, 9.12, 'peter', [11, 22, 33])
# print(type(tupleA))
# print(tupleA)
# 元组的查询
# for item in tupleA:
#     print(item,end=' ')
# print(tupleA[2])
print(tupleA[::-2])  # 表示反转字符串，每隔两个取一次
print(tupleA[-2:-1:])   # 倒着取下标 为 -2 到 -1区间的

print(tupleA[-4:-1:])

tupleA[4][0] = 285202   #可以对元组中的列表进行修改
print(tupleA)

tupleB = (1,)
print(type(tupleB))

tupleC = (1,2,3,4,3,4,4,1) #tuple(range(10))
print(tupleC.count(4))


