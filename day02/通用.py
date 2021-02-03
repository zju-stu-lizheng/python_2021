'''
共有方法 ： + * in
'''
strA = '人生苦短'
strB = '我用python'
# 合并 +
print(strA+strB)
# 复制 *
print(strA*3)
# in 对象是否存在
listA = list(range(1,20))
print('生' in strA)
print(22 in listA)

dictA={"name":"peter"}
print("name" in dictA)
