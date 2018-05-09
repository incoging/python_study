# coding=utf-8
# with语句的使用

# 先来一个例子
# #文件处理
# file = open("./foo.txt")
# data = file.read()
# file.close()
#
# #带有判断的加强版
# file = open("./foo.txt")
# try:
#     data = file.read()
# finally:
#     file.close()

# 使用with语句的
# with open("./foo.txt") as file:
#     data = file.read()
"""
with所求值的对象必须有一个__enter__()方法，一个__exit__()方法
紧跟with后面的语句被求值后，返回对象的__exit__()方法被调用，这个方法的返回值将被赋值给as后面的变量，
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
"""


# class Sample:
#     def __enter__(self):
#         print("In __enter__()")
#         return "Foo"
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("In __exit__()")
#
# def get_sample():
#     return Sample()
#
# with get_sample() as sample:
#     print("sample:", sample)
'''
output:
In __enter__()
sample: Foo
In __exit__()

所以根据执行结果可以看到：
1.__enter__()函数被执行
2.__enter__()的返回值"Foo",赋值给了变量"sample"
3.执行代码块，打印"sample:"以及sample的值
4.__exit__()方法被执行
'''


# with处理异常
# __exit__方法有三个参数- val, type 和 trace。 这些参数在异常处理中相当有用。
class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        # print("trace:", trace)

    def do_something(self):
        bar = 1 / 0
        return bar + 10


with Sample() as sample:
    sample.do_something()
'''
type: <class 'ZeroDivisionError'>
Traceback (most recent call last):
value: division by zero
  File "X:/jet_python/study/python_study/python/with_study.py", line 66, in <module>
trace: <traceback object at 0x0000011B926F6088>
    sample.do_something()
  File "X:/jet_python/study/python_study/python/with_study.py", line 62, in do_something
    bar = 1 / 0
ZeroDivisionError: division by zero
'''
'''
这个例子中，with后面的get_sample()变成了Sample()。这没有任何关系，
只要紧跟with后面的语句所返回的对象有 __enter__()和__exit__()方法即可。
此例中，Sample()的__enter__()方法返回新创建的Sample对象，并赋值给变量sample。

实际上，在with后面的代码块抛出任何异常时，__exit__()方法被执行。正如例子所示，异常抛出时，
与之关联的type，value和stack trace传给__exit__()方法，因此抛出的ZeroDivisionError异常被打印出来了。
开发库时，清理资源，关闭文件等等操作，都可以放在__exit__方法当中。
'''
