#####2.1.1 字符串与字节、字典
1.python3中str是唯一能够保存文本信息的数据类型，保存的是Unicode码位。
* 区别：Python2用str表示字节字符串

bytes，bytearray 与str不同，它们只能用字节作为序列值，即0 <= x < 256.
```python
>>> print(bytes([102, 111, 111]))
b'foo'
```
同时它们在转换为另一种序列类型时可以显示其原面目：
```python
>>> list(b'foo bar')
[102, 111, 111, 32, 98, 97, 114]
>>>tuple(b'foo bar')
(102, 111, 111, 32, 98, 97, 114)
```
2.可以用单引号，双引号，三引号加 b 或 B 前缀来表示字节、字节字符串。
>Unicode包含无法用字节表示的“抽象”文本，因此，编码为二进制数据才能存储，网络发送。

将字符串编码为字节序列：
```python
str.encode(encoding='utf-8', errors='strict')  # encoding 编码格式， errors 错误处理方案
or 
bytes(source,encoding, errors)  # source 表示str，这个方法encoding无默认值
```
二进制数据转换为字符串：
```python
bytes.decode(encoding, errors)
or 
str(source, encoding, errors)
```
>Notice: python3中字符串初始化后是不可改变的。

3.字符串拼接
```python
"".join(substring)  # ""中是拼接时连接的东西
>>> ','.join(['some', 'comma', 'separated'])
'some,comma,separated'
```

4.列表推导
```python
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6 ,8]
```

5.enumerate(枚举) 方便获取元素下标
```python
>>> for index, element in enumerate(['one', 'tow', 'three']):
        print(index, element)
0 one
1 two
2 three
```
6.zip() 一个一个合并多个列表
```python
>>> for item in zip([1, 2, 3], [4, 5, 6]):
    print(item)
(1, 2)
(3, 4)
(5, 6)
```
对zip()的结果再次调用zip()，可以将其恢复原状：
```python
>>> for item in zip(*zip([1, 2, 3], [4, 5, 6])):
        print(item)
(1, 2, 3)
(4, 5, 6)
```
7.字典
```python
>>> squares = {num: num ** 2 for num in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
>Notice: 字典不会按照键的添加顺序来保存元素，如果非要按序保存，可使用OrderedDict
```python
>>> from collections import OrderedDict
>>> OrderedDict(str(number), None) for number in range(5)).keys()
odict_keys(['0', '1', '2', '3', '4'])
```