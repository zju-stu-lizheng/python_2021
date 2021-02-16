# Numpy学习笔记

1. `Python`中的列表保存的是对象的指针。因此为了保存一个简单的列表，如`[1,2,3]`，则需要三个指针和三个整数对象
2. `numpy`提供了两种基本的对象：
   * `ndarray`：是存储单一数据类型的多维数组
   * `ufunc`：是一种能够对数组进行处理的特殊函数

## 一、ndarray

### 1. ndarray 对象的内存结构

1. `ndarray`对象在内存中的结构如下：


```python
import numpy as np
a = np.array([[0,1,2],[3,4,5],[6,7,8]],dtype=np.float32)
print(a.dtype,a.ndim,a.shape,a.strides,a.data)
```

```python
float32 2 (3, 3) (12, 4) <memory at 0x00000207FDB87AC8>
```

可以看到：该数组中元素类型为` float32` ；该数组有2 个轴。每个轴的长度都是 3 个元素。第 0 轴增加1时，下标增加 12字节（也就是 3个元素，即一行的距离）； 第 1 轴增加 1时，下标增加 4字节（也就是⼀个元素的距离）。 

2.  修改数组的内容时，会直接修改数据存储区域。所有使⽤该数据存储区域的数组都将被同时修改！

```python
a = np.arange(0,4)
b = a.reshape((2,2))
```

```python
[0 1 2 3]
[[0 1]
 [2 3]]
```

```python
print(a.flags.owndata,b.flags.owndata)
```

```python
True False
```

```python
print(b.base is a)
```

```python
True
```

#### 1.1 dtype

1. `numpy`有自己的浮点数类型: `float16/float32/float64/float128`

   * 在需要指定` dtype` 参数时，你可以使⽤` numpy.float16` ，也可以传递⼀个表示数值类型的字符串。`numpy` 中的每个数值类型都有⼏种字符串表示。字符串和类型之间的对应关系都存储在`numpy.typeDict `字典中。

2. 使⽤` ndarray.astype()` ⽅法可以对数组元素类型进⾏转换。

   

#### 1.2 shape

1. 你可以使用`ndarray.reshape()`方法调整数组的维度
   * 你可以在某个维度设置长度为-1，此时该维度的长度会自动计算
2. 你可以直接修改` ndarry` 的 `shape` 属性，此时直接修改原始数组

#### 1.3 view

1. 我们可以通过 ndarray.view() ⽅法，从同⼀块数据区创建不同的 dtype 数组。即使⽤不同的数值类型查看同⼀段内存中的⼆进制数据。它们使⽤的是同⼀块内存。 
#### 1.4 strides

1. 我们可以直接修改 `ndarray` 对象的 strides 属性。此时修改的是原始数组。


2. 你可以使⽤ `np.lib.stride_tricks.as_stride()` 函数创建⼀个不同 strides 的视图。

#### 1.5 拷贝和视图

1. 当处理` ndarray `时，它的数据存储区有时被拷⻉，但有时并不被拷⻉。有三种情况。
   * 完全不拷贝：简单的赋值操作，这种情况下是新的变量引用`ndarray`对象
   * 视图和浅拷⻉：不同的` ndarray `可能共享相同的数据存储区。如` ndarray.view() `⽅法创建⼀个新的`ndarray` 但是与旧 `ndarray` 共享相同的数据存储区。新创建的那个数组称作视图数组。 
   * 深拷⻉： `ndarray.copy()` 操作会返回⼀个完全的拷⻉，不仅拷⻉` ndarray `也拷⻉数据存储区。


### 2. 数组的创建

1. 浙里有几个共同参数
   * `a` ：⼀个 `array-like` 类型的实例，它不⼀定是数组，可以为 `list` 、 `tuple` 、 `list of tuple` 、`list of list` 、 `tuple of list` 、 `tuple of tuple `等等。
   * `dtype` ：数组的值类型，默认为 float 。你可以指定 Python 的标准数值类型，也可以使⽤ `numpy`的数值类型如： `numpy.int32` 或者 `numpy.float64 `等等。
   * `order` ：指定存储多维数据的方式。 
     * 可以为 'C' ，表示按⾏优先存储（C⻛格）； 
     * 可以为 'F' ，表示按列优先存储（Fortran⻛格）。 
     * 对于 **_like() 函数， order 可以为： 'C' ， 'F' ， 'A' （表示结果的 order 与 a 相 同）， 'K' （表示结果的 order 与 a 尽可能相似）
   * `subok` ： `bool` 值。如果为 True 则：如果 a 为` ndarray` 的⼦类（如 matrix 类），则结果类型与 a 类型相同。如果为 False 则：结果类型始终为 `ndarray` 。默认为 True 。

#### 2.1 创建全1或者全0

1. `np.empty`(shape[,dtype,order]) ：返回⼀个新的 `ndarray` ，指定了 shape 和 `dtype` ，但是没有初始化元素。因此其内容是随机的。

```python
import numpy
result = numpy.empty((2,2),order='C')
type(result)
<class 'numpy.ndarray'>

result
array([[8.03269123e-312, 8.03269120e-312],
       [8.03269123e-312, 8.03269123e-312]])

result2 = numpy.empty_like(result) # 创建一个与result一样的
type(result2)
<class 'numpy.ndarray'>

result2
array([[8.03269123e-312, 8.03269120e-312],
       [8.03269123e-312, 8.03269123e-312]])

result3 = numpy.empty_like([1,2,3])  # array_like对象
type(result3)
<class 'numpy.ndarray'>
result3
array([-1818459832,       32765, -1909780624])
```

2. `np.eye(N[, M, k, dtype])` ：返回⼀个⼆维数组，对⻆线元素为1，其余元素为0。 M 默认等于 N 。 k默认为0表示对⻆线元素为1，如为正数则表示对⻆线上⽅⼀格的元素为1，如为负数表示对⻆线下⽅⼀格的元素为1.

```python
numpy.eye(2,M=3) # 2*3
array([[1., 0., 0.],
       [0., 1., 0.]])
numpy.eye(3,k=1)	# 对角线上一格全1
array([[0., 1., 0.],
       [0., 0., 1.],
       [0., 0., 0.]])
numpy.eye(3,k = -1) # 对角线下一格全1
array([[0., 0., 0.],
       [1., 0., 0.],
       [0., 1., 0.]])
numpy.identity(3) # 单位矩阵
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

3.  `np.ones(shape[, dtype, order]) `：返回⼀个新的 `ndarray `，指定了 shape 和 type ，每个元素初始化为1.

```python
r = numpy.ones((2,3))
type(r)
<class 'numpy.ndarray'>
r
array([[1., 1., 1.],
       [1., 1., 1.]])
r2= numpy.ones_like(r) # 与r维度一样，全1
type(r2)
<class 'numpy.ndarray'>
r2
array([[1., 1., 1.],
       [1., 1., 1.]])
r3 = numpy.ones_like([(1,2),(3,4)]) # array_like为元组的列表
type(r3)
<class 'numpy.ndarray'>
r3
array([[1, 1],
       [1, 1]])
```

4. `np.zeros(shape[, dtype, order])` ：返回⼀个新的 `ndarray `，指定了 shape 和 type ，每个元素初始化为0.

```python
r = numpy.zeros((2,3))
type(r)
<class 'numpy.ndarray'>
r
array([[0., 0., 0.],
       [0., 0., 0.]])
r2 = numpy.zeros_like(r)
r2
array([[0., 0., 0.],
       [0., 0., 0.]])
r3 = numpy.zeros_like([(1,2),(3,4)])
r3
array([[0, 0],
       [0, 0]])
```

5. ` np.full(shape, fill_value[, dtype, order])` ：返回⼀个新的`ndarray `，指定了 shape 和type ，每个元素初始化为 fill_value 。

```python
r = numpy.full((2,3),999,dtype = 'int32')
r
array([[999, 999, 999],
       [999, 999, 999]])
r2 = numpy.full_like(r,fill_value = 10,dtype='int32')
r2
array([[10, 10, 10],
       [10, 10, 10]])
r3 = numpy.full_like([(1,2),(3,4)],fill_value = 10,dtype='int32')
r3
array([[10, 10],
       [10, 10]])
```

#### **2.2** 从现有数据创建 

1. `np.array(object[, dtype, copy, order, subok, ndmin]) `:从 object 创建。
   * object 可以是⼀个 `ndarray` ，也可以是⼀个 array_like 的对象，也可以是⼀个含有返回⼀个序列或者 `ndarray` 的 __array__ ⽅法的对象，或者⼀个序列。
   * copy ：默认为 True ，表示拷⻉对象
   * order 可以为 'C'、'F'、'A' 。默认为 'A' 。
   * `subok` 默认为 False
   * `ndmin` ：指定结果 `ndarray` 最少有多少个维度。 

2. `np.asarray(a[, dtype, order]) `：将 a 转换成⼀个 `ndarray `。其中 a 是 array_like 的对象， 可以是 list 、 list of tuple 、 tuple 、 tuple of list 、 `ndarray` 类型。 order 默认为 C 。 

3. `np.asanyarray(a[, dtype, order])` ：将 a 转换成 `ndarray` 。 

4. `np.ascontiguousarray(a[, dtype]) `：返回C⻛格的连续` ndarray`

5. `np.asmatrix(data[, dtype])` ：返回 matrix

6. `np.copy(a[, order])` ：返回` ndarray` 的⼀份深拷⻉ 

7. `np.frombuffer(buffer[, dtype, count, offset])` ：从输⼊数据中返回⼀维 `ndarray `。 count 指定读取的数量， -1 表示全部读取； offset 指定从哪⾥开始读取，默认为0。创建的数组与 buffer 共享内存.uffer 是⼀个提供了 buffer 接⼝的对象（内置的 bytes/bytearray/array.array 类型提供了该接⼝）。

8. `np.fromfile(file[, dtype, count, sep])` ：从⼆进制⽂件或者⽂本⽂件中读取数据返回`ndarray `。 sep ：当从⽂本⽂件中读取时，数值之间的分隔字符串，如果 sep 是空字符串则表示⽂件应该作为⼆进制⽂件读取；如果 sep 为 " " 表示可以匹配0个或者多个空⽩字符。 

9. `np.fromfunction(function, shape, **kwargs)` ：返回⼀个 `ndarray` 。从函数中获取每⼀个坐标点的数据。假设 shape 的维度为N，那么 function 带有 N 个参数， fn(x1,x2,...x_N) ，其返回值就是该坐标点的值。

10. `np.fromiter(iterable, dtype[, count]) `：从可迭代对象中迭代获取数据创建⼀维 `ndarray `。

```python
r = numpy.array([1,2,3,4])
r
array([1, 2, 3, 4])
r2 = numpy.asarray([1,2,3,4])
r2
array([1, 2, 3, 4])
r3=numpy.asanyarray([1,2,3,4])
r3
array([1, 2, 3, 4])
r4=numpy.ascontiguousarray([1,2,3,4])
r4
array([1, 2, 3, 4])
r5=numpy.asmatrix([1,2,3,4])
r5
matrix([[1, 2, 3, 4]])
from array import array
arr = array('d',[1,2,3,4])
a=numpy.frombuffer(arr,dtype=numpy.float)
arr
array('d', [1.0, 2.0, 3.0, 4.0])
a
array([1., 2., 3., 4.])
a.flags.owndata
False
```

11. np.fromstring(string[, dtype, count, sep]) ：从字符串或者 raw binary 中创建⼀维ndarray 。如果 sep 为空字符串则 string 将按照⼆进制数据解释（即每个字符作为 ASCII 码值对待）。创建的数组有⾃⼰的数据存储区。
12. np.loadtxt(fname[, dtype, comments, delimiter, ...]) :从⽂本⽂件中加载数据创建 ndarray ，要求⽂本⽂件每⼀⾏都有相同数量的数值。 comments ：指示注释⾏的起始字符，可以为单个字符或者字符列表（默认为 # ）。 delimiter :指定数值之间的分隔字符串，默认为空⽩符。 converters ：将指定列号(0,1,2...)的列数据执⾏转换，是⼀个 map ，如 {0:func1} 表示对第⼀列数据执⾏ func1(val_0) 。skiprows ：指定跳过开头的多少⾏。 usecols ：指定读取那些列（0表示第⼀列）。

#### 2.3 从数值区间创建

1. np.arange([start,] stop[, step,][, dtype]) :返回均匀间隔的值组成的⼀维 ndarray 。区间是半闭半开的 [start,stop) ，其采样⾏为类似Python的 range 函数。 start 为开始点， stop 为终⽌点,step 为步⻓，默认为1。这⼏个数可以为整数可以为浮点数。注意如果 step 为浮点数，则结果可能有误差，因为浮点数相等⽐较不准确。 

2. np.linspace(start, stop[, num, endpoint, ...]) ：返回 num 个均匀采样的数值组成的⼀维ndarray （默认为50）。区间是闭区间 [start,stop] 。 endpoint 为布尔值，如果为真则表示 stop 是最后采样的值（默认为 True ），否则结果不包含 stop 。 retstep 如果为 True 则返回结果包含采样步⻓ step ，默认为 True 。 

3. np.logspace(start, stop[, num, endpoint, base, ...]) ：返回对数级别上均匀采样的数值组成的⼀维 ndarray 。采样点开始于 base^start ，结束于 base^stop 。 base 为对数的基，默认为 10。 它逻辑上相当于先执⾏ arange 获取数组 array ，然后再执⾏ base^array[i] 获取采样点它没有 retstep 关键字参数

```python
r = numpy.arange(0,10) # 不包含终点
r
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
r2 = numpy.linspace(0,10,num=5,endpoint=True,retstep=True)
r2
(array([ 0. ,  2.5,  5. ,  7.5, 10. ]), 2.5)
r3=numpy.linspace(0,10,num=5,endpoint=False,retstep=False)
r3
array([0., 2., 4., 6., 8.])
r4=numpy.logspace(0,10,base=2,num=5) # 基数为2，默认包含终点
r4
array([1.00000000e+00, 5.65685425e+00, 3.20000000e+01, 1.81019336e+02,
       1.02400000e+03])
```

### 3.数组的索引

#### 3.1 一维数组的索引

1. ⼀维数组的索引和列表相同。假设 a1 是⼀维数组 
   * 可以指定⼀个整数 i 作为索引下标，如 a1[i]
   * 可以指定⼀个切⽚作为索引下标，如 a1[i:j] 。通过切⽚获得的新的数组是原始数组的⼀个视图，它与原始数组共享相同的⼀块数据存储空间。 
