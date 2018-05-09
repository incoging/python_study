#### 广播(BroadCasting)
广播(BroadCasting)是指Numpy在算术运算期间可以处理不同形状数组的能力。

##### 先介绍一下数组直接相乘和点乘的区别<br/>

普通的数组、矩阵对应相乘
```
import numpy as np
# 1. 数组相乘
a1 = np.array([1, 2, 3, 4])
a2 = np.array([10, 20, 30, 40])
print('a1对应乘以a2的结果是: \n', a1*a2)

output:
a1对应乘以a2的结果是: [ 10  40  90 160]
```

矩阵乘法
```
import numpy as np
# a1,a2为二维矩阵
a1 = np.array([[1, 2], [2, 2]])
a2 = np.array([[2, 2], [2, 2]])
# .dot为矩阵乘法，若a1和a2为两个向量，那么.dot的结果为一个数值。
res = a1.dot(a2)
print(res)

output:
[[6 6]
 [8 8]]
```

##### 不同形状数组相乘
```
# a是 4x3 的矩阵
a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
# b是 1x3 的矩阵
b = np.array([1.0, 2.0, 3.0])
print('First array : \n', a)
print('Second array : \n', b)
print('First Array + Second Array: \n', a+b)

output:
First array :
 [[ 0.  0.  0.]
 [10. 10. 10.]
 [20. 20. 20.]
 [30. 30. 30.]]
Second array :
 [1. 2. 3.]
First Array + Second Array:
 [[ 1.  2.  3.]
 [11. 12. 13.]
 [21. 22. 23.]
 [31. 32. 33.]]
```
实现广播需要遵循的规则：<br/>
1.让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐<br/>
2.输出数组的shape是输入数组shape的各个轴上的最大值<br/>
3.如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错<br/>
4.当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值