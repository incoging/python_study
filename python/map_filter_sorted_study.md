#### map 函数
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，返回一个Iterator对象。
```python
def square(x):
    return x * x
res = map(square, [1, 2, 3, 4, 5, 6])
print(list(res))
```

#### reduce函数
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做函数运算，其效果就是：
```python
from functools import reduce
reduce(func, [x1, x2, x3, x4]) = func(func(func(x1,x2), x3), x4) 
```
把[1, 3, 5, 7, 9]变为13579
```python
from functools import reduce
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])
'''
output:
13579
'''
```
* 实例：
```python
# 把str转化为int
from functools import reduce
def fn(x, y):
    return x * 10 + y
def char2num(c):  # 利用字典将字符转变为数字
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]
num = map(char2num, '13579')
result = reduce(fn, num)
'''
outpu:
13579
'''
```
>整理成str2int为：
```python
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(c):
        return DIGITS[c]
    return reduce(fn, map(char2num, s))
```

#### filter 函数
一般用于过滤序列：filter()接收一个函数和一个序列，把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。返回一个Iterator对象。
```python
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
'''
output:
[1, 3, 5, 7, 9]
'''
```
* 实例
```python
# 取素数
# 构造一个从3开始的奇数数列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0  # 如果x不能整除n，那么返回True


# 定义一个生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break
```
#### sorted 函数
sorted可以比较数字、字符串、字典等。
```python
sorted([36, 5, -12, 9, -21])
'''output:
[-21, -12, 5, 9, 36]
'''
```
可以接收一个参数key函数，将此函数应用于序列的每一个值
```python
sorted([36, 5, -12, 9, -21], key=abs)
'''output:
[5, 9, -12, -21, 36]
'''
```
若要反向排序，传入第三个参数reverse=True即可：
```python
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
'''output:
['Zoo', 'Credit', 'bob', 'about']
'''
```