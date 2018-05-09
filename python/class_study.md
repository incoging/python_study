### class 
#### __init__ 函数
将类实例化时,会创建一个空的类实例,一般的 Python 类的定义中会有一个特殊的方法来初始化,这个方法就是__init__()
当调用了类的实例化方法后,\__init__()方法会立刻被这个类的实例调用。
所以,\__init__()不是构造函数,而是一个普通的方法.可以说是构造方法。
```python
class FirClass: 

    # 前面没有self，此时的定义count相当于全局变量，所以两次调用A()，第二次输出2
    # 若写成self.count = 0，则每次实例化count都会置为0
    count = 0
    
    def __init__(self):
        FirClass.count += 1

    def output(self):
        print(self.count)


obj1 = FirClass()
obj1.output()  # output: 1
obj2 = FirClass()
obj2.output()  # output 2
```
\__init__()方法可以有参数，参数通过__init__()传递到时类的实例化操作上
```python
class SecClass:
    def __init__(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part


obj3 = SecClass(2.0, 6.3)
print(obj3.r, obj3.i)  # 输出结果：2.0 6.3
```
> __init__方法的第一个参数是self,表示创建的实例本身，而非类。
```python
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


objT = Test()
objT.prt()
"""
output:
<__main__.Test object at 0x000001D8248A49E8>
<class '__main__.Test'>
从以上可以看出：
1.self代表的是类的实例，代表类对象的地址;
2.而self.__class__则指向类。
3.self不是python关键字，我们把它换成TaoBao也是可以正常执行的。
"""
```
#### 内部变量类型:
```python
class People:
    # 定义基本属性,此处定义为类属性
    name = ""
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问， 私有属性以两个下划线开头。
    __weight = 0

    # 定义特殊变量，即以双下划线开头和结尾的变量，这种变量在外部是可以直接访问的。
    __brithday__ = "1993-12-01"
    # 定义实例属性
    def __init__(self, sex):
        self.sex = sex
```

#### 继承:
```
class DerivedClassName(BaseClassName1):
    <statement-1>
    ...
    ...
    <statement-N>
"""
需要注意圆括号中的基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索，
即方法在子类中未找到时，从左到右查找基类中是否包含方法。
BaseClassName1必须与派生类定义在一个作用域内，除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用：
class DerivedClassName(modname.BaseClassName):
"""    
```

#### 方法重写:
```python
class Parent:
    def my_method(self):
        print("调用父类方法。")


class Child(Parent):
    def my_method(self):
        print("调用子类方法。")


c = Child()
c.my_method()  # output: 调用子类方法。
```
#### 类的专有方法：
```
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
```
#### 运算符重载:
```python
class Person:  # 针对__str__的重载
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)


per1 = Person('孙悟空', 999)
print(per1)
"""
output:
这个人的名字是孙悟空,已经有999岁了！
如果没有重载函数的话输出的就是一串看不懂的字符串：
<__main__.people object at 0x00000272A730D278>
"""
```
对加法的重载
```python
class Vector:  # 针对__add__的重载
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
```

#### 动态绑定:
Python是动态语言，创建一个class实例后，可以给该实例绑定任何属性和方法。
```
class Student(object):
    psss

>>> s = Student()
>>> s.name = "Michael"  # 动态给实例绑定一个属性
>>> print(s.name)
Michael
```
>还可以给实例绑定一个方法
```
>>> def set_age(self, age):  # 定义一个函数作为实例方法
...     self.age = set_age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
>>> s.set_age(25)  # 调用实例方法
>>> s.age  # 测试结果
25
```
> 对一个实例绑定的方法对于其他实例是不可用的，因此，可以给class绑定方法,之后所有实例均可用
```
>>> def set_score(self, score):
...     self.score = score
... 
>>> Student.set_score = set_score
```

#### \__slots__ 限制实例属性
例如：只允许对Student实例添加name和age属性
```
# 在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ("name", "age")  # 用tuple定义允许绑定的属性名称

>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'，试图绑定score将得到AttributeError的错误。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```
* Notice：_slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

#### @staticmethod
返回函数的静态方法。
```
class C(object):
    @staticmethod
    def func(arg1, arg2, ...):
        ...
```
以上实例声明了静态方法 func，类可以不用实例化就可以调用该方法 C.func()，
当然也可以实例化后调用 C().func()。


#### @property 负责把一个方法变成属性调用
```
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 上面@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
# 于是，我们就拥有一个可控的属性操作

>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```
定义只读属性：
```python
# 只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```
>关于@property @x.setter @x.deleter   
1).只有@property表示只读。   
2).同时有@property和@x.setter表示可读可写。   
3).同时有@property和@x.setter和@x.deleter表示可读可写可删除。


