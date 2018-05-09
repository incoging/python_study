## 数组处理

1.改变形状
* reshape() --- Gives a new shape to an array without changing its data
* flat() --- A 1-D iterator over the array
* flatten() --- Returns a copy of the array collapsed into one dimension
* ravel() --- Returns a contiguous flattened array

2.转置操作
* transpose() --- Permutes the dimensions of an array
* ndarray.T() --- Same as self.transpose()
* rollaxis() --- Rolls the specified axis backwards
* swapaxes() --- Interchanges the two axes of an array

3.修改维度
* broadcast() --- Produces an object that mimics broadcasting
* broadcast_to() --- Broadcasts an array to a new shape
* expand_dims() --- Expands the shape of an array
* squeeze() --- Removes single-dimensional entries from the shape of an array

4.数组连接
* concatenate() --- Joins a sequence of arrays along an existing axis
* stack() --- Joins a sequence of arrays along a new axis
* hstack() --- Stacks arrays in sequence horizontally (column wise)
* vstack() --- Stacks arrays in sequence vertically (row wise)

5.数组分割(Splitting arrays)
* split() --- Splits an array into multiple sub-arrays
* hsplit() --- Splits an array into multiple sub-arrays horizontally (column-wise)
* vsplit() --- Splits an array into multiple sub-arrays vertically (row-wise)

6.添加、删除元素(Adding/removing elements)
* resize() --- Returns a new array with the specified shape
* append() --- Appends the values to the end of an array
* insert() --- Inserts the values along the given axis before the given indices
* delete() --- Returns a new array with sub-arrays along an axis deleted
* unique() --- Finds the unique elements of an array


### 第四部分

1.np.concatenate(a_tuple, axis=0, out=None)
矩阵拼接
* a_tuple 为要拼接的矩阵或向量列表
* axis 设定要拼接的维度，对于二维矩阵来说，0为按行拼接，1为按列拼接

```
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[11,21,31],[7,8,9]])
res1 = np.concatenate((a,b),axis=0)
print(res1)
print("结果形状：", res1.shape)

output:
[[ 1  2  3]
 [ 4  5  6]
 [11 21 31]
 [ 7  8  9]]
结果形状： (4, 3)


res2 = np.concatenate((a,b),axis=1)
print(res2)
print("结果形状：", res2.shape)

output:
[[ 1  2  3 11 21 31]
 [ 4  5  6  7  8  9]]
结果形状： (2, 6)
```

### 第五部分

1.np.split() 数组分割
```
split(ary,indices_or_sections,axis=0)
```
* ary 要分割的数组
* indices_or_sections 要分割为几段
* axis 切割哪一维度
> indices_or_sections 若为一个列表的话，如[3, 5, 6, 10]，则切割为，0-2，3-4, 5, 6-9 这四部分

eg:
```
>>> x = np.arange(9.0)
>>> np.split(x, 3)
[array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.,  8.])]

>>> x = np.arange(8.0)
>>> np.split(x, [3, 5, 6, 10])
[array([ 0.,  1.,  2.]), array([ 3.,  4.]), array([ 5.]), array([ 6.,  7.]), array([], dtype=float64)]
```

2.numpy.array_split() 数组分割

```
numpy.array_split(ary, indices_or_sections, axis=0)
```
与np.split()的区别，这个函数允许要分割的维度除以indices_or_sections，除不尽。

eg:
```
>>> x = np.arange(8.0)
>>> np.array_split(x, 3)
[array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.])]
```