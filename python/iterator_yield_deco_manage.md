##### 2.2.1 迭代器
迭代器是一个实现了迭代器协议的容器对象，基于以下两个方法：
```
__next__: 返回容器的下一个元素
__iter__: 返回迭代器本身
```
迭代器遍历完序列时。会引发一个StopIteration异常，因此可以和循环兼容，后捕获这个异常结束循环。   
创建迭代器类:
```
class CountDown:
    def __init__(self,step):
        self.step = step
    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        """Return the iterator itself."""
        return self
```
```
>>> for elem in CountDown(4):
        print(elem)
3
2
1
0      
```
判断一个对象是否为可迭代对象或是否为可迭代对象，用collections模块的Iterable类型，和Iterator类型判断：
```
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True

>>> from collections import Iterator
>>> isinstance('abc', Iterator) # str是否是Iterator对象
Flase
>>> isinstance(1,2,3], Iterator) # list是否是Iterator对象
Flase
```
>即：list、dict、str可以迭代，但不是Iterator对象，即，它们可以用for循环进行遍历，但不能用next()函数，
同时它们可以用iter()函数使之变为Iterator对象。
```
>>> from collections import Iterator
>>> isinstance(iter(1,2,3]), Iterator)
True
```


#### 2.2.2 yield 语句
```
def fibon(max):
    n = 0  # 用来控制输出次数
    a, b = 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

>>> for n in fibon(5):
        print(n)
1
1
2
3
5
```
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
如上，调用 fibon(5) 不会执行 fibon 函数，而是返回一个 iterator 对象！所以也可以利用该对象的next()方法：
```
>>> f = fibon(5)
>>> f.next() 
1 
>>> f.next() 
1 
>>> f.next() 
2 
>>> f.next() 
3 
>>> f.next() 
5 
>>> f.next() 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
StopIteration
```
>一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，
下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
每次中断都会通过 yield 返回当前的迭代值。
* Notice:fibon 是一个 generator function，而 fibon(5) 是调用 fibon 返回的一个 generator，

#### 2.2.3 generator(生成器)
生成器：一边循环，一边计算。
```
gen = (x * x for x in range(5))  # gen即为一个生成器。
# 要打印gen的内容，可以通过next()函数获得gen的下一个返回值：
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
4
>>> next(gen)
9
>>> next(gen)
16
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
>因为generator也是可迭代对象，所以可以用for循环来访问gen的内容
```
>>> g = (x * x for x in range(10))
>>> for n in g:
        print(n)
0
1
4
9
16  # 在for循环内不需要再管理StopIteration错误。
```
> 上面的For循环调用generator，得不到generator的return语句返回值。
要想得到返回值，就得捕获StopIteration错误，返回值包含在StopIteration的value中：
```
>>> gen = fibon(6)
>>> while True:
        try:
            x = next(gen)
            print("gen:", x)
        except StopIteration as e:
            print("Generator return Value:", e.value）
            break
gen: 1
gen: 1
gen: 2
gen: 3
gen: 5
gen: 8
Generator return value: done            
```


可以用isgeneratorfunction来判断一个函数是不是特殊的generator函数：
```
>>> from inspect import isgeneratorfunction
>>> isgeneratorfunction(fibon)
True
```


