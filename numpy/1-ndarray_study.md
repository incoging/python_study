#### Numpy 简介
Numpy -- Numerical Python 是一个基于Python的可以存储和处理大型矩阵的库。

##### NaN
NaN, Not a Number, 非数. 它即不是无穷大, 也不是无穷小, 而是python/numpy/... 觉得无法计算时返回的一个符号

##### Ndarray对象
Ndarray -- N-dimensional array type N维数组模型，ndarray的本质是数组，但它支持数组里面嵌套数组。
```
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```
* dtype: 数组元素类型
* copy: 默认值为True，对象被复制
* order: 默认为'K', C(行)，F(列)，A(Any)(default)
* subok：默认情况下，强制类型转换为基类数组
* ndmin：返回指定数组的最小维度

例子：
```
import numpy as np
a1 = np.array([1,2,3])
a2 = np.array([[1,2],[3,4]]) # 输出二维数组
a3 = np.array([1,2,3,4,5],ndmin=2) # 数组维数=2
a4 = np.array([1,2,3],dtype = complex) # 指定数据类型为复数
print("a1 = ",a1)
print("a2 = ",a2)
print("a3 = ",a3)
print("a4 = ",a4)

output:
a1 =  [1 2 3]
a2 =  [[1 2]
 [3 4]]
a3 =  [[1 2 3 4 5]]
a4 =  [1.+0.j 2.+0.j 3.+0.j]
```
ndarray常用方法：
* reshape(...)    返回一个给定shape的数组副本
* resize(...)     将原数组shape改变形状
* flatten()/ravel()    返回一个展平的数组，原数组不变
* astype(dtpye)    返回指定元素类型的数组副本
* fill()   将数组元素全部设定为一个标量值
* sum()/Prod()    计算所有数组元素的和/积
* mean()/var()/std()    计算数组元素的均值/方差/标准差
* max()/min()/ptp()median()    返回数组元素的最大值/最小值/取值范围/中位数
* argmax()/argmin()    返回最大值/最小值的索引
* sort(axis=-1, kind='quicksort', order=None)    对数组进行排序，axis指定排序的轴，kind指定排序算法，
-1 表示最后一维
* view()/copy()    view创造一个新的数组对象指向同一数据，copy是深复制
* tolist()    将数组完全转为列表
* compress(condition, axis=None, out=None)    返回满足条件的元素构成的数组

##### 数据类型
五种基本数据类型
* bool 布尔
* int 整型 (int, intc, intp, int8,int 16, int32, int64)
* uint 无符号整型 (uint8, uint16, uint32, uint64)
* float 浮点型 (float, float16, float32, float64)
* complex 复数 (complex, complex64,complex128)
```
import numpy as np
z1 = np.arange(3, dtype=np.float) # float类型
z2 = np.arange(3, dtype=np.intc) # int型
z3 = np.arange(3, dtype=np.complex) #复数complex
print("z1 = ",z1)
print('z2 = ',z2)
print("z3 = ",z3)

output:
z1 =  [0. 1. 2.]
z2 =  [0 1 2]
z3 =  [0.+0.j 1.+0.j 2.+0.j]
```

数组类型也可以由字符代码指定：

```
import numpy as np
z1 = np.arange(3, dtype=np.float)
print("z1 = ",z1)
# 数组类型由字符代码指定---f等同于float32
z4 = np.array([1, 2, 3],dtype='f')
print('z4 = ',z4)
```

数据类型转换：

```
import numpy as np
#　数据类型转换
z1 = np.arange(3)
z2 = np.float32(z1)
print('z1_type = ',z1.dtype)#获取z1的数据类型
print('z2_type = ',z2.dtype)#获取z2的数据类型
print('z1 = ',z1)
print('z2 = ',z2)

output:
z1_type =  int32
z2_type =  float32
z1 =  [0 1 2]
z2 =  [0. 1. 2.]

```

##### ndarray属性
* dtpye  数组元素的类型
* shape  数组形状
* ndim  数组维度
* size  数组中元素的个数
* itemsize  数组元素所占字节数
* T  数组的转置
* flat  返回一个数组的迭代器，对flat赋值将导致整个数组的元素被覆盖
* real/imag  复数数组的实部/虚部
* nbytes  数组占用的存储空间

##### 创建数组

1.np.empty() -- 创建一个指定shape和类型的空数组
```
# numpy.empty(shape, dtype = float, order = 'C')

import numpy as np
a1 = np.empty([3,2], dtype=int)
#数组中的元素是随机生成的
print('a1 = ', a1)
```

2.np.zeros() -- 创建一个指定shape和类型的全零数组
```
a2 = np.zeros((3, 2), dtype=[('x', 'f'),('y', 'i4')])
# [x(float), y(int)]
print('a2 = ', a2)

output:
a2 =  [[(0., 0) (0., 0)]
 [(0., 0) (0., 0)]
 [(0., 0) (0., 0)]]
```

3.np.ones() -- 创建一个指定shape和类型的全1数组
```
a3 = np.ones([2,4], dtype=complex)
print('a3 = ', a3)

output:
a3 =  [[1.+0.j 1.+0.j 1.+0.j 1.+0.j]
 [1.+0.j 1.+0.j 1.+0.j 1.+0.j]]
```

从现有数据创建数组<br/>

4.np.asarray(a, dtype = None, order = None)

> Notice: array和asarray都可以将结构数据转化为ndarray，
但是主要区别就是当数据源是ndarray时，array仍然会copy出一个副本，占用新的内存，但asarray不会。
```
import numpy as np
# 将list 转化为 ndarray
a1 = np.asarray([1, 2, 3], dtype = float)
print('a1 = ', a1)
 # 将list of tuple转化为ndarray
a2 = np.asarray([(5, 2, 0), (8, 9)])
print('a2 = ', a2)

output:
a1 =  [1. 2. 3.]
a2 =  [(5, 2, 0) (8, 9)]
```

5.np.fromiter(iterable, dtype, count = -1) -- 从一个可迭代对象创建一个数组
```
print('a3 = ', range(5))
a4 = np.fromiter(iter(range(5)), dtype=float)
print('a4 = ', a4)

output:
a3 =  range(0, 5)
a4 =  [0. 1. 2. 3. 4.]
```

从数值域创建数组

6.np.arange(start, stop, step, dtype) -- 创建在给定范围内具有均匀间隔的ndarray对象
```
a1 = np.arange(3, 18, 3, dtype = float)
print('a1 = ', a1)

output:
a1 =  [ 3.  6.  9. 12. 15.]
```

7.np.linspace(start, stop, num, endpoint, retstep, dtype)
  -- 类似于np.arange(),不同的是这个指出了给定范围内均匀间隔值的数量
```
a2 = np.linspace(1, 2, 5, endpoint = False)
print('a2 = ', a2)

output:
a2 =  [1.  1.2 1.4 1.6 1.8]
```

8.np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
  -- 创建在指定范围有均匀间隔的数字对应的对数
```
a3 = np.logspace(1.0, 2.0, num = 10, base = 2)
print('a3 = ', a3)

output:
a3 =  [2.         2.16011948 2.33305808 2.5198421  2.72158    2.93946898
 3.1748021  3.42897593 3.70349885 4.        ]
```


