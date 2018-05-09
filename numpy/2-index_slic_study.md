#### 索引
实现索引的三种基本方法：字段访问，基本切片，高级索引

```
import numpy as np
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('a2 =\n ', a2, )
print('Now we will slice array a2 from index a2[1:]\n', a2[1:])
print('得到索引为1所在的列的值（第二列）:　\n', a2[...,1])
print('得到索引为1所在的行的值（第二行）: \n', a2[1,...])
print('得到第二列及其后面的值: \n',a2[...,1:])

output:
a2 =
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Now we will slice array a2 from index a2[1:]
 [[4 5 6]
 [7 8 9]]
得到索引为1所在的列的值（第二列）:　
 [2 5 8]
得到索引为1所在的行的值（第二行）:
 [4 5 6]
得到第二列及其后面的值:
 [[2 3]
 [5 6]
 [8 9]]
```

#### 高级索引
##### 整型索引
基于 N 维索引来获取数组中任意元素。 每个整数数组表示该维度的下标值。

通过两个数组分别表示要取出的行和列的下标。
```
import numpy as np
a1 = np.array([[1, 2], [3, 4], [5, 6]])
print('a1 = ', a1)
selection = a1[[0,1,2], [0,1,0]]
print('索引为：(0,0),(1,1),(2,0)的元素是：\n', selection)

output:
a1 =  [[1 2]
 [3 4]
 [5 6]]
索引为：(0,0),(1,1),(2,0)的元素是：
 [1 4 5]
```

将通过行列选出来的元素直接组成一个数组
```
a2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('a2 = ', a2)
# 对应的方式是，第0行第一列；第0行第二列，第3行第0列，第3行第二列。
Rows = np.array([[0, 0], [3, 3]])
Cols = np.array([[0, 2], [0, 2]])
print('The selection result from a2 = \n', a2[Rows, Cols])

output:
a2 =  [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
The selection result from a2 =
 [[ 0  2]
 [ 9 11]]
```

##### 布尔索引
根据条件的结果，返回满足条件的数值

例子1：
```
a1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('a1 = \n', a1)
# 使用布尔索引， 输出大于5的item
print('The items greater than 5 are: \n', a1[a1 > 5])

output:
The items greater than 5 are:
 [ 6  7  8  9 10 11]
```

例子2：过滤非复数元素
```
a2 = np.array([8, 8+9j, 9, 9+8j])
print('数组中的复数元素为: \n', a2[np.iscomplex(a2)])

output：
数组中的复数元素为:
 [8.+9.j 9.+8.j]
```