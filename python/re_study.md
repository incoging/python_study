#### 正则表达式
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。(import re)

##### re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
```
re.match(pattern, string, flags=0)
```
* pattern: 匹配的正则表达式
* string:  要匹配的字符串
* flags:   标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

匹配成功re.match方法返回一个匹配的对象，否则返回None。
```
import re

result1 = re.match('www', 'www.runoob.com')
print(result1.span())
result2 = re.match('com', 'www.runoob.com')
print(result2)

output:
(0, 3)
None
```

可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
```
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
```
实例：
```
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)  # 前面加一个r，表示这个字符串是原生字符串，字符串里面的内容将不会被转译

if matchObj:
    print("matchObj.group() : ", matchObj.group())  # 返回匹配到的整个表达式的字符串
    print("matchObj.group() : ", matchObj.groups())  # 返回包含所有小组字符串的元组
    print("matchObj.group(1) : ", matchObj.group(1))  # 返回获取到的第一个小组字符串的内容
    print("matchObj.group(2) : ", matchObj.group(2))  # 返回获取到的第二个小组字符串的内容
else:
    print("No match!!")

output:
matchObj.group() :  Cats are smarter than dogs
matchObj.group() :  ('Cats', 'smarter')
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```

##### re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配。返回一个匹配的对象，否则返回None。
```
re.search(pattern, string, flags=0) # 参数含义如上
```
实例：
```
import re

print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())
"""
span(),用于返回所匹配的结果第一个字符在原字符串的索引，和最后一个字符在原字符串中的索引+1 的位置：即：
(子串第一个字符的索引, 子串最后一个字符的索引+1)
"""
output:
(0, 3)
(11, 14)
```
re.search 也可以用group函数，如下：
```
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")

output:
searchObj.group() :  Cats are smarter than dogs
searchObj.group(1) :  Cats
searchObj.group(2) :  smarter
```

##### re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

##### compile 函数

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
```
re.compile(pattern[,flags])
```
* pattern: 一个字符串形式的正则表达式
* flags： 可选，表示模式匹配，比如忽略大小写，多行模式等。
>> flags具体参数：<br/>
re.I  忽略大小写 <br/>
re.L  表示特殊字符集\w, \W, \b, \B, \s, \S 依赖于当前环境 <br/>
re.M  多行模式 <br/>
re.S  相当于 "." + 换行符  （因为"."不包括换行符）<br/>
re.U  表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库 <br/>
re.X 为了增加可读性，忽略空格和' # '后面的注释

实例:
```
>>>import re
>>> pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
>>> m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
>>> print m                                         # 返回一个 Match 对象
<_sre.SRE_Match object at 0x10a42aac0>
>>> m.group(0)   # 可省略 0   group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
'12'
>>> m.start(0)   # 可省略 0   start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
3
>>> m.end(0)     # 可省略 0   end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
5
>>> m.span(0)    # 可省略 0   span([group]) 方法返回 (start(group), end(group))。
(3, 5)
```

另一个实例：
用圆括号分组匹配
```
>>>import re
>>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
>>> m = pattern.match('Hello World Wide Web')
>>> print m                               # 匹配成功，返回一个 Match 对象
<_sre.SRE_Match object at 0x10bea83e8>
>>> m.group(0)                            # 返回匹配成功的整个子串
'Hello World'
>>> m.span(0)                             # 返回匹配成功的整个子串的索引
(0, 11)
>>> m.group(1)                            # 返回第一个分组匹配成功的子串
'Hello'
>>> m.span(1)                             # 返回第一个分组匹配成功的子串的索引
(0, 5)
>>> m.group(2)                            # 返回第二个分组匹配成功的子串
'World'
>>> m.span(2)                             # 返回第二个分组匹配成功的子串
(6, 11)
>>> m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
('Hello', 'World')
>>> m.group(3)                            # 不存在第三个分组
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
```


##### 检索和替换
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
```
re.sub(pattern, repl, string, count=0)
```
* pattern: 正则中的模式字符串
* repl: 替换的字符串，也可以为一个函数
* string: 要被查找替换的原始字符串
* count: 模式匹配后替换的最大次数，默认0表示替换所有的匹配

实例：
```
import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)

output:
电话号码 :  2004-959-559
电话号码 :  2004959559
```
当repl为一个函数：
```
# 将字符串中匹配到的数字乘以2
import re

# 定义数字乘于 2 函数
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

output:
A46G8HFD1134
```

##### findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
> 注意，match和search都是返回对象，这里返回列表

```
findall(string[, pos[, endpos]])
```
* string： 待匹配的字符串
* pos： 可选参数，指定开始匹配的起始位置，默认为0，若为其他数字，则包括该数字所指索引
* endpos: 可选参数，指定开始匹配的结束位置，默认为字符串的长度, 若为其他数字，则不包括该数字所指索引

实例：
```
import re

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

Output:
['123', '456']
['88', '12']
```

##### re.finditer函数

和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
```
re.finditer(pattern, string, flags=0)
```
* pattern	匹配的正则表达式
* string	要匹配的字符串。
* flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。

实例：
```
import re

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )

Output:
12
32
43
3
```