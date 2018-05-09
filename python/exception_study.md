#### 异常处理

##### try语句
```
try:
    statement1
except ErrorType:
    statement2
else:
    statement3
finally:
    statement4( f.close() )
```
执行顺序：
* 首先，执行try子句（statement1）
* 如果没有异常发生，忽略except子句，接着执行else语句。(else子句将在try子句没有发生任何异常的时候执行。)
* 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，
  那么对应的except子句将被执行。最后执行 try 语句之后的代码。
* 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
* 总是会执行finally子句，不管有没有发生异常，finally一般都用于如上括号中示范的典型用处
> 1. 一个try语句可能包含多个except子句，分别来处理不同的特定情况，最多只有一个分支会被执行。
> 2. 再次注意else子句将在try子句没有发生任何异常的时候执行。

一个except可以同时处理多个异常
```
except(RuntimeError, TypeError, NameError):
    pass
```

##### 抛出异常
可以使用raise抛出一个异常
```
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: HiThere
```
> raise 后的唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果只想知道这是否抛出了一个异常，并不想去处理它，那么用一个简单的 raise 语句就可以再次把它抛出。
```
>>> try:
        raise NameError('HiThere')
    except NameError:
        print('捕获了NameError异常!')
        raise

捕获了NameError异常!
Traceback (most recent call last):
  File "<stdin>", line 2, in ?
NameError: HiThere
```

##### 用户自定义异常
用户可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承。
```
>>> class MyError(Exception):
        def __init__(self, value): # 覆盖默认的__init__方法
            self.value = value
        def __str__(self):
            return repr(self.value)

>>> try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)

My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'
```
当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，
然后基于这个基础类为不同的错误情况创建不同的子类。
```
class Error(Exception):
    """所建立的模块的基本错误类型"""
    pass

class InputError(Error):
    """抛出输入错误

        属性:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """抛出进行不允许转换的转换操作错误

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```


##### python 标准异常

```
BaseException               所有异常的基类
SystemExit                  解释器请求退出
KeyboardInterrupt           用户中断执行(通常是输入^c)
Exception                   常规错误的基类
StopIteration               迭代器没有更多的值
GeneratorExit               生成器发生异常来通知退出
StandardError               所有內建标准异常的基类
ArithmeticError             所有数值计算错误类的基类
FloatingPointError          浮点计算错误
OverflowError               数值运算超出最大限制
ZeroDivisionError           除零错误
AssertionError              断言语句失败
AttributeError              对象没有这个属性
EOFError                    没有內建输入，到达EOF标记
EnvironmentError            操作系统错误类的基类
IOError                     输入/输入操作失败
OSError                     操作系统错误
WindowsError                系统调用失败
ImportError                 导入模块/对象失败
LookupError                 无效数据查询的基类
IndexError                  序列中没有此索引
KeyError                    映射中没有这个键
MemoryError                 内存溢出错误
NameError                   未声明/初始化对象
UnboundLocalError           访问未初始化的本地变量
ReferenceError              弱引用试图访问已经垃圾回收了的对象
RuntimeError                一般的运行时错误
NotImplementedError         尚未实现的方法 
SyntaxError                 Python语法错误
IndentationError            缩进错误
TabError                    Tab和空格混用
SystemError                 一般的解释器系统错误
TypeError                   对类型无效的操作
ValueError                  传入无效的参数
UnicodeError                Unicode 相关的错误
UnicodeDecodeError          Unicode 解码时的错误
UnicodeEncodeError          Unicode 编码时错误
UnicodeTranslateError       Unicode 转换时错误
Warning                     警告的基类
DeprecationWarning          关于被弃用的特征的警告
FutureWarning               关于构造将来语义会有改变的警告
OverflowWarning             旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning   关于特性将会被废弃的警告
RuntimeWarning              可疑的运行时行为(runtime behavior)的警告
SyntaxWarning               可疑的语法的警告
UserWarning                 用户代码生成的警告
```
