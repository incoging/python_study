#### 装饰器
本质上，decorator是一个返回函数的高阶函数。
```
# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把decorator置于函数的定义处
@log
def now():
    print('2018-08-08')
    
# 调用now()函数
>>> now()  #  此时实际上相当于执行的wrapper函数
call now():
2018-08-08
```
把@log放到now()函数的定义处，相当于执行了语句
```
now = log(now)
```
>由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，
首先打印日志，再紧接着调用原始函数。

因为函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
它们的__name__已经从原来的'now'变成了'wrapper'
```
>>> now.__name__
'wrapper'
```
>因为返回的那个wrapper()函数名字就是'wrapper'，
所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
Python内置的functools.wraps可以把原始函数的__name__等属性制到wrapper()函数中：
```
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数：
```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```
用法如下：
```
@log("execute")
def now():
    print('2018-08-08')
    
>>>now()
execute now():
2018-08-08
```
和两层嵌套的decorator相比，3层的是：
```
>>> now = log("execute")(now)
```
>上面语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，
参数是now函数，返回值最终是wrapper函数。

同样使用functools.wraps的格式：
```
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```