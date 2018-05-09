#### join用法
Python中有join()和os.path.join()两个函数：
* join(): 将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
* os.path.join(): 将多个路径组合后返回

1.join函数
```python
'sep'.join(sequence) # 返回一个以分隔符sep连接各个元素后新的字符串
# sep: 分隔符，可以为空
# sequence: 要连接的元素序列、字符串、元组、字典
```
例子：
```
s = "abc"
res = ','.join(s)
print(res)

output:
a,b,c
```

2.os.path.join()函数
```python
os.path.join(path1[,path2[,......]])  # 将多个路径组合后返回
```
