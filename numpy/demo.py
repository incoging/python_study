from numpy import *
import numpy as np

# numpy的数组类被称为ndarray，别名为array。numpy.array与标准python库类array.array不一样，标准库类中的那个只能处理一维数组
# 并且功能很少。ndarray有以下一些属性：
#
a = arange(15).reshape(3, 5) #numpy提供一个类似于range的函数，返回一个数组，参数为（起始，结束，步长）
print(a)
print(a.shape)   # 显示数组a的形状
print(a.ndim)    # 显示数组的维度，即几维数组
print(a.dtype)    # 显示数组中的元素类型
print(a.itemsize)    # 显示数组中每个元素的字节大小
print(type(a))    # 显示数组a的类型，为numpy.ndarray
'''
output:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
(3, 5)
2
int32
4
<class 'numpy.ndarray'>
'''
#如果用的是numpy数组,想要完全打印变量的值而不用省略号,那么在打印前加上:
#np.set_printoptions(threshold=np.inf)

# 构建数组
# 可以通过一个使用array函数的Python列表或元组来构建。同时可以通过调用生成后数组的属性dtype来了解该数组的元素类型。
# b = array([2, 3, 4])  # 等于 b = array((2, 3, 4))
# print(b)
# print(b.dtype)
# c = array([1.5, 2.3, 5.6])
# print(c)
# print(c.dtype)

# 可以在创建数组的时候显式的指定数组类型
# d = array([[1, 3], [5, 6]], dtype = complex)
# print(d)

# z = zeros((2,3))  #生成一个2行3列的全零数组
# print(z)
# o = ones((2, 3, 4), dtype = int16)  #生成一个3维的全1数组，并指明元素类型为int16，若不指明，默认为float64
# e = empty((2, 3))   #生成一个初始化内容为随机并且依赖于内存状态的数组。
# line = linspace(0, 2, 9)  # 返回一个包含9个元素的数组，其参数为（起始，结束，元素个数）
# print(line)  # [ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.  ]
# print(line.dtype)  # float64

# 打印数组
# 如果一个数组太大以至于无法打印，numpy会自动跳过中间部分只打印角部分，若想强制打印整个数组，可以改变打印的选项
# set_printoptions(threshold="nan")


# 数组操作
# 数组上的算术操作是逐元素的，
# A = array([[1, 1], [0, 1]])
# B = array([[2, 0], [3, 4]])
# print(A - B)   #[[-1, 1], [-3, -3]]
# print(A * B)   #[[2, 0], [0, 4]]
# #若想使用矩阵的乘积，可以使用dot函数来实现
# value = dot(A, B)
# print(value)   #[[5, 4], [3, 4]]

# axis参数可以把运算应用到数组指定的轴上
# b = arange(12).reshape(3, 4)
# print(b)
# '''
# b = [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# '''
#
# b1 = b.sum(axis = 0)     #每一列的和
# print(b1)
# '''
# b1 = [12 15 18 21]
# '''
#
# b2 = b.min(axis = 1)   #每一行的最小值
# print(b2)
# '''
# b2 = [0 4 8]
# '''
#
# b3 = b.cumsum(axis = 1)   #按行累加求和
# print(b3)
# '''
# b3 = [[ 0  1  3  6]
#  [ 4  9 15 22]
#  [ 8 17 27 38]]
# '''

# a = arange(10) ** 3
# print(a)
# a[:6:2] = -1000  # 相当于a[0:6:2] = -1000  从0开始到第6位(不包括第6位)，每2个元素设置为-1000
# print(a)  # [-1000     1 -1000    27 -1000   125   216   343   512   729]
# b = a[::-1]     #相当于反转a    [729 512 343 216 125  64  27   8   1   0]
# print(b)


# 多维数组的索引
# def f(x,y):
#     return 10*x+y
# b = fromfunction(f,(5,4),dtype=int)    #由f函数生成5行4列的一个数组
'''
b = [[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]]
'''
'''
>>> b[2,3]
23
>>> b[0:5, 1]                       # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[ : ,1]                        # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, : ]                      # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
'''
# 当少于轴数的索引被提供时，缺失的索引被认为是整个切片：
# >>> b[-1]                                  # the last row. Equivalent to b[-1,:]
# array([40, 41, 42, 43])
a = np.array()

np.concatenate()