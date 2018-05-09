#### 数组迭代
Numpy包含一个迭代对象：numpy.nditer. 可以实现多维数组的迭代。

1.使用nditer迭代输出一个3x4的数组
```
a1 = (np.arange(0, 60, 5)).reshape(3,4)
print('原始数组为 :\n', a1)
print('迭代输出这个数组:')
for x in np.nditer(a1):
    print(x, end = ' ')

output:
原始数组为 :
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
迭代输出这个数组:
0 5 10 15 20 25 30 35 40 45 50 55
```
> Notice: 迭代的顺序是和数组内存布局一致的，而不是使用标准C或者Fortran顺序。

验证迭代顺序：
```
# 产生一个2x3的数组
a = np.arange(6).reshape(2, 3)
# 迭代输出数组a
for x in np.nditer(a):
    print x,
print "\n"
# 输出a的转置
for x in np.nditer(a.T):
    print x,
print "\n"
# 输出a的转置的深copy对象的内容
for x in np.nditer(a.T.copy(order = 'C')):
    print x,

output:
0 1 2 3 4 5

0 1 2 3 4 5

0 3 1 4 2 5
```
> 注解：a和a.T的遍历顺序是一样的，也就是他们在内存中的存储顺序也是一样的，
但是a.T.copy(order = 'C')的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的。默认是按行访问。

nditer提供了一种顺序参数（order parameter）的方法来实现这一要求。默认情况下是order = 'K'， 就是上述的访问方式。
另外有：order = 'C'和order = 'F'。不妨理解为：C是按行访问，F是按列访问。<br/>
利用order强制更改迭代顺序：
```
a = np.arange(6).reshape(2, 3)
for x in np.nditer(a, order = 'C'):
    print(x, end = ' ')
print('\n')
for x in np.nditer(a, order = 'F'):
    print(x, end = ' ')

output:
0 1 2 3 4 5

0 3 1 4 2 5
```

#### 迭代修改数组值
默认情况下，nditer将输入数组视为只读对象。要修改数组元素，必须指定读写（ read-write）或只写（write-only）模式。
即nditer有一个可选的参数为op_flags,其默认值为只读(read-only)
```
a = np.arange(6).reshape(2, 3)
print a

for x in np.nditer(a, op_flags = ['readwrite']):
    x[...] = 2*x
print a

output:
[[0 1 2]
 [3 4 5]]
[[ 0  2  4]
 [ 6  8 10]]
```
[...]的解释：
一般而言，Python中的赋值只需更改本地或全局变量字典中的引用，而不是修改现有变量。
这意味着简单地赋值给x将不会将值放入数组的元素中，而是将x从数组元素引用切换为对您分配的值的引用。
要实际修改数组的元素，x应该用省略号索引。

##### 广播迭代
具有广播特性的两个数组，可以使用nditer同时迭代：
```
import numpy as np
# 建立两个shape不一样的数组
a1 = (np.arange(0, 60, 5)).reshape(3,4)
a2 = np.array([1, 2, 3, 4], dtype = int)
print('原始数组 a1 是 :\n', a1, '\n原始数组 a1 是: \n', 'a2')

# 广播迭代
print('迭代一起输出a1和a2: \n')
for x,y in np.nditer([a1, a2]):
    print("%d : %d"%(x,y), end = ' ')

output:
原始数组 a1 是 :
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
原始数组 a2 是:
 [1 2 3 4]
迭代一起输出a1和a2:
0 : 1 5 : 2 10 : 3 15 : 4 20 : 1 25 : 2 30 : 3 35 : 4 40 : 1 45 : 2 50 : 3 55 : 4
```