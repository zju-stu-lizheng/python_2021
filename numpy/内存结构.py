import numpy as np
a = np.array([[0,1,2],[3,4,5],[6,7,8]],dtype=np.float32)
# print(a.dtype,a.ndim,a.shape,a.strides,a.data)

#修改数组的内容时，会直接修改数据存储区域。
#所有使⽤该数据存储区域的数组都将被同时修改！
# a = np.arange(0,4)
# b = a.reshape((2,2))
# print(a)
# print(b)
# print(a.flags.owndata,b.flags.owndata)
# print(b.base is a)
# b[0][0] = 100
# print(a,b)  # 发现a，b同时变动
# a[-1] = -1
# print(a,b)

# print(np.typeDict)

# 使⽤ ndarray.astype() ⽅法可以对数组元素类型进⾏转换。
# b = a.astype(dtype=np.int32)
# print(b.dtype,b,a,sep='\n')

# 你可以使用`ndarray.reshape()`方法调整数组的维度
# aa = np.arange(0,8)
# print(aa.ndim,aa.shape,aa.strides)
# bb = aa.reshape((2,4))
# print(bb.ndim,bb.shape,bb.strides)

# 通过 ndarray.view() ⽅法，从同⼀块数据区创建不同的 dtype 数组
# b = a.view(np.uint8)
# c = a.view(np.uint32)
# print(b,c)

# 直接修改 ndarray 对象的 strides 属性
# print(a)
# a.strides = (4,4)
# print(a)

# 使⽤ np.lib.stride_tricks.as_stride() 函数创建⼀个不同 strides 的视图
# b = np.lib.stride_tricks.as_strided(a,strides=(4,4))
# print(a,b)

b = a  # 完全不拷贝
print(b is a)   # True

c = a.view()  # 创建视图
print(c.base is a, a.base, c.flags.owndata)  # True None False

f = a.copy()  # 完全拷贝
print(f.base,f.flags)