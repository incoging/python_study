### lambda

python 使用lambda来创建匿名函数<br>
lambda只是一个表达式，函数体比def简单很多<br>
lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。<br>

```
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为：", sum(10, 20))
```

##### lambda与列表推导
```
data = range(10)
funcs = [lambda x: i * x for i in data]
for func in funcs:
    print(func(2), ",",end="")
"""
output:
18 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,18 ,
"""
```
>解析：
funcs是一个列表，列表里的每一个元素是个lambda function，
Python的闭包(lambda和function等)会保存变量的名字(i)和scoping(global)。当你调用的时候才会去找具体的对象。
给i赋不同的值，在调用时会去取最新的i值

##### 更改：
```
data = range(10)

funcs = [lambda x, y=i: y * x for i in data]

i = 12345
for func in funcs:
    print(func(2), ",", end="")

"""
output:
0 ,2 ,4 ,6 ,8 ,10 ,12 ,14 ,16 ,18 ,
"""
```
>解析：
这里给lambda多一个参数，这个参数每次传递一个默认值，这个默认值由每次的i指定，所以funcs列表中的
lambda函数都有一个默认值，理解下面的for i in data的意思

for i in data 等价于：
```
iterator = iter(data)
i = next(iterator)
# do something
i = next(iterator)
# do something
...
＃ raise StopIteration
```