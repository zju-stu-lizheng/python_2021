# for循环
# 语法特点:遍历操作，依次地取集合容器中的每个词
# for i in range(10):
#     print(i)
'''
sum = 0
for data in range(1, 101):  # 左包含，右边不包含
    sum += data
    pass
print("sum=", sum, sep='')
'''

# break和continue
# break 表示中断结束  满足条件直接的结束本层循环
# continue:结束本次循环，继续进行下次循环
# 这两类关键字只能用在循环中

# sum = 0
# for item in range(1, 51):
#     if sum > 100:
#         print('循环执行到%d就退出'%item)
#         break  # 退出循环体
#         pass
#     sum += item
#     pass
# print("sum=%d" % sum)
# print('continue的使用')
# for item in range(1, 100):  # 求出来奇数
#     if item % 2 == 0:
#         continue
#         print("在continue的后面会不会执行呢")
#         pass
#     print(item)
#     pass
'''
for item in 'I love python':
    if item == 'o' or item == ' ':
        continue
    print(item, end='')
    pass
'''
