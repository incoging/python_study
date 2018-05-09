### 内置函数

#####  all()函数
用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False
或者 iterable 是否为空，如果是返回 True，否则返回 False。
```
all(iterable)
```
* iterable -- 元组或列表。
> Notice: 空元组、空列表返回值为True，这里要特别注意。

实例：
```
>>>all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True
>>> all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
False
>>> all([0, 1，2, 3])          # 列表list，存在一个为0的元素
False

>>> all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
>>> all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
False
>>> all((0, 1，2, 3))          # 元组tuple，存在一个为0的元素
False

>>> all([])             # 空列表
True
>>> all(())             # 空元组
True
```

##### any()函数
判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，
若有一个元素不为空, 0, false,则返回True.
```
any(iterable)
```
* iterable -- 元组或列表
> Notice: 注意和all()函数的区别，all()表示所有，any() 表示存在。

实例：
```
>>> any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True
>>> any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
True
>>> any([0, '', False])        # 列表list,元素全为0,'',false
False
>>> any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
>>> any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
True
>>> any((0, '', False))        # 元组tuple，元素全为0,'',false
False
>>> any([]) # 空列表
False
>>> any(()) # 空元组
False
```


##### bin()函数
返回一个整数 int 或者长整数 long int 的二进制表示。
实例：
```
>>>bin(10)
'0b1010'
>>> bin(20)
'0b10100'
```


##### callable()函数
用于检查一个对象是否是可调用的。如果返回True, object仍然可能调用失败，
如果返回False,调用对象object绝对不会成功。
对于函数，方法，lambda函数，以及实现了__call__方法的类实例，它都返回True.

实例：
```
>>>callable(0)
False
>>> callable("testing")
False

>>> def add(a, b):
...     return a + b
...
>>> callable(add)             # 函数返回 True
True
>>> class A:                  # 类
...     def method(self):
...             return 0
...
>>> callable(A)               # 类返回 True
True
>>> a = A()
>>> callable(a)               # 没有实现 __call__, 返回 False
False
>>> class B:
...     def __call__(self):
...             return 0
...
>>> callable(B)
True
>>> b = B()
>>> callable(b)               # 实现 __call__, 返回 True
True
```


##### compile()函数
将一个字符串编译为字节代码。
```
compile(source, filename, mode[, flags[, dont_inherit]])
```
* source -- 字符串或者AST（Abstract Syntax Trees）对象。。
* filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
* mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
* flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
* flags和dont_inherit是用来控制编译源码时的标志

实例：
```
>>>str = "for i in range(0,10): print(i)"
>>> c = compile(str,'','exec')   # 编译为字节代码对象
>>> c
<code object <module> at 0x10141e0b0, file "", line 1>
>>> exec(c)
0
1
2
3
4
5
6
7
8
9
>>> str = "3 * 4 + 5"
>>> a = compile(str,'','eval')
>>> eval(a)
17
```


##### dir()函数
返回模块的属性列表。
```
dir([object])
```
* object -- 对象、变量、类型。

1. 不带参数时，返回当前范围内的变量、方法和定义的类型列表；<br/>
2. 带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。<br/>
如果参数不包含__dir__()，该方法将最大限度地收集参数信息。<br/>

实例：
```
>>>dir()   #  获得当前模块的属性列表
['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
>>> dir([ ])    # 查看列表的方法
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__',
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__',
'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
```


##### divmod()函数
把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
```
divmod(a, b)
```
* a: 数字
* b: 数字

实例：
```
>>> divmod(7, 2)
(3, 1)
>>> divmod(8, 2)
(4, 0)
>>> divmod(1+2j,1+0.5j)
((1+0j), 1.5j)
```


##### enumerate()函数
将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标。
```
enumerate(sequence, [start=0])
```
* sequence -- 一个序列、迭代器或其他支持迭代对象。
* start -- 下标起始位置。

实例：
```
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>>list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>>list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

>>>seq = ['one', 'two', 'three']
>>>for i, element in enumerate(seq):
...    print(i, seq[i])
...
0 one
1 two
2 three
```


##### eval()函数
执行一个字符串表达式，并返回表达式的值。
```
eval(expression[, globals[, locals]])
```
* expression -- 表达式。
* globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
* locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。


实例：
```
>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> n=81
>>> eval("n + 4")
85
```


##### exec()函数
执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
```
exec(object[, globals[, locals]])
```
* object：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。如果object是一个字符串，该字符串会先被解析为一组Python语句，然后在执行（除非发生语法错误）。如果object是一个code对象，那么它只是被简单的执行。
* globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
* locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals相同的值。
> Notice: exec的返回值永远是None，而eval()返回表达式的计算结果

实例1：
```
>>>exec('print("Hello World")')
Hello World

#  多行语句字符串
>>> exec ("""for i in range(5):
...     print ("iter time: %d" % i)
... """)
iter time: 0
iter time: 1
iter time: 2
iter time: 3
iter time: 4
```

实例2：
```
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})

func()

output:
60
33
34
```
> 解析：exec后面跟参数形式，只能改变表达式之外的变量值。


##### format 格式化函数
```
str.format()
```
实例：
```
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'

>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'

>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
```
> 通过字典设置参数
```
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
```
> 通过列表索引设置参数
```
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
```
> 传入对象
```
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
```
* 数字格式化
```
3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
-1	{:+.2f}	-1.00	带符号保留小数点后两位
2.71828	{:.0f}	3	不带小数
5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)
5	{:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
10	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
1000000	{:,}	1,000,000	以逗号分隔的数字格式
0.25	{:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
13	{:10d}	        13	右对齐 (默认, 宽度为10)
13	{:<10d}	13	左对齐 (宽度为10)
13	{:^10d}	    13	中间对齐 (宽度为10)

'{:b}'.format(11)       1011
'{:d}'.format(11)       11
'{:o}'.format(11)       13
'{:x}'.format(11)       b
'{:#x}'.format(11)      0xb
'{:#X}'.format(11)      0XB
```
说明：<br/>
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

\+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

> 使用大括号{}来转义大括号：
```
>>> print ("{} 对应的位置是 {{0}}".format("runoob"))
runoob 对应的位置是 {0}
```


##### frozenset()函数
返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。如果不提供任何参数，默认会生成空集合。
```
frozenset([iterable])
```
* iterable -- 可迭代的对象，比如列表、字典、元组等等。

实例：
```
>>>a = frozenset(range(10))     # 生成一个新的不可变集合
>>> a
frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = frozenset('runoob')
>>> b
frozenset(['b', 'r', 'u', 'o', 'n'])   # 创建不可变集合
```


##### getattr()函数
返回一个对象属性值。
```
getattr(object, name[, default])
```
* object -- 对象。
* name -- 字符串，对象属性。
* default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

实例：
```
>>>class A(object):
...     bar = 1
...
>>> a = A()
>>> getattr(a, 'bar')        # 获取属性 bar 值
1
>>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'bar2'
>>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
3
```

##### hex()函数
用于将10进制整数转换成16进制，以字符串形式表示。
```
hex(x)
```
* x -- 10进制整数

实例：
```
>>> hex(-42)
'-0x2a'
>>> hex(12)
'0xc'
>>> type(hex(12))
<class 'str'>      # 字符串
```


##### id()函数
用于获取对象的内存地址。

实例：
```
>>> a = 'runoob'
>>> id(a)
4531887632
>>> b = 1
>>> id(b)
140588731085608
```


##### issubclass()函数
判断一个类是否是另一个类的子类
```
issubclass(class, classinfo)
```
判断class是否是classinfo的子类，是返回True，否则返回False
```
class A:
    pass
class B(A):
    pass

print(issubclass(B,A))    # 返回 True
```


##### iter()函数
用来生成迭代器,返回迭代器对象
```
iter(object[, sentinel])
```
* object -- 支持迭代的集合对象。
* sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。

实例：
```
>>>lst = [1, 2, 3]
>>> for i in iter(lst):
...     print(i)
...
1
2
3
```


##### locals()函数
以字典类型返回当前位置的全部局部变量。
对于函数, 方法, lambda 函式, 类, 以及实现了 \__call__ 方法的类实例, 它都返回 True。

实例：
```
>>>def runoob(arg):    # 两个局部变量：arg、z
...     z = 1
...     print (locals())
...
>>> runoob(4)
{'z': 1, 'arg': 4}      # 返回一个名字/值对的字典
```

##### next()函数
返回迭代器的下一个项目。
```
next(iterator[, default])
```
* iterator -- 可迭代对象
* default -- 可选，用于设置在没有下一个元素时返回该默认值，
如果不设置，又没有下一个元素则会触发 StopIteration 异常。

实例：
```
# 获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```


##### oct()函数
将一个整数转换成8进制字符串。
实例：
```
>>>oct(10)
'012'
>>> oct(20)
'024'
>>> oct(15)
'017'
>>>
```


##### ord()函数
以一个字符(长度为1的字符串)作为参数，返回对应的ASCII数值，或者Unicode数值，
如果所给的Unicode字符超出了Python定义范围，则引发一个TypeError异常。

实例：
```
>>>ord('a')
97
>>> ord('b')
98
>>> ord('c')
99
```


##### pow()函数
求解x的y次方的值
```
1.
pow(x, y[, z])
2.
import math
math.pow(x,y)
```
计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
> Notice: pow()通过内置的方法直接调用，内置方法会把参数作为整型，而math模块会把参数转换为float。

实例：
```
import math   # 导入 math 模块

print ("math.pow(100, 2) : ", math.pow(100, 2))
# 使用内置，查看输出结果区别
print ("pow(100, 2) : ", pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2))
print ("pow(2, -1) : ", pow(2, -1))
print ("math.pow(3, 0) : ", math.pow(3, 0))

output：
math.pow(100, 2) :  10000.0
pow(100, 2) :  10000
math.pow(100, -2) :  0.0001
pow(2, -1) : 0.5
math.pow(3, 0) :  1.0
```


##### range()函数
Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型，
所以打印的时候不会打印列表。
Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表
，返回的变量类型为列表。
```
range(stop)
range(start, stop[, step])
```
* start: 计数从 start 开始。默认是从 0 开始。
* stop: 计数到 stop 结束，但不包括 stop。
* step：步长，默认为1。

实例：
```
>>>range(5)
range(0, 5)
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(0))
[]
```


##### setattr()函数
setattr 函数对应函数 getattr()，用于设置类的属性值，该属性必须存在。
```
setattr(object, name, value)
```
* object -- 对象。
* name -- 字符串，对象属性。
* value -- 属性值。

实例：
```
>>>class A(object):
...     bar = 1
...
>>> a = A()
>>> getattr(a, 'bar')          # 获取属性 bar 值
1
>>> setattr(a, 'bar', 5)       # 设置属性 bar 值
>>> a.bar
5
```


##### sorted()函数
对所有可迭代的对象进行排序操作。
```
sorted(iterable, key=None, reverse=False)
```
* iterable -- 可迭代对象。
* key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
指定可迭代对象中的一个元素来进行排序。
* reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）
> Notice: sort 与 sorted 区别：<br/>
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。<br/>
list 的 sort 方法返回的是对原列表进行操作，而sorted 方法返回的是一个新的 list，
而不是在原来的基础上进行的操作。

实例：
```
>>>sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]                      # 默认为升序
# 若不再需要原来的列表，则list.sort()方法会效率更高一点。
>>>a=[5,2,3,1,4]
>>> a.sort()
>>> a
[1,2,3,4,5]
# 利用key值进行倒序排列
>>>example_list = [5, 0, 6, 1, 2, 7, 3, 4]
>>> result_list = sorted(example_list, key=lambda x: x*-1)
>>> print(result_list)
[7, 6, 5, 4, 3, 2, 1, 0]

```


##### sum()函数
对元组、列表求和, 返回计算结果
```
sum(iterable[, start])
```
* iterable -- 可迭代对象，如列表。
* start -- 指定相加的参数，如果没有设置这个值，默认为0

实例：
```
>>>sum([0,1,2])
3
>>> sum((2, 3, 4), 1)        # 元组计算总和后再加 1
10
>>> sum([0,1,2,3,4], 2)      # 列表计算总和后再加 2
12
```


##### vars()函数
返回对象object的属性和属性值的字典对象。如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
```
vars([object])
```
* object -- 对象

实例：
```
>>>print(vars())
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> class Runoob:
...     a = 1
...
>>> print(vars(Runoob))
{'a': 1, '__module__': '__main__', '__doc__': None}
>>> runoob = Runoob()
>>> print(vars(runoob))
{}
```


##### zip()函数
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
> Notice: 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
利用 * 号操作符，可以将元组解压为列表。
```
zip([iterable, ...])
```
* iterabl -- 一个或多个迭代器;

实例：
```
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
```