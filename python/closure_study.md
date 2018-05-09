#### 函数作为返回值
```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n 
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
# 调用lazy_sum函数时返回的不是求和结果，而是求和函数
print(f)
'''output:
<function lazy_sum.<locals>.sum at 0x000001F8DA420620>
'''
# 调用函数f，得到真正的计算结果：
print(f())
25
```
> 当我们调用lazy_sum时，每次都会返回一个新的函数
```
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
```

* Notice：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：
```python
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
# 调用上面的函数：
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```