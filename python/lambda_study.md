### lambda

python ʹ��lambda��������������<br>
lambdaֻ��һ�����ʽ���������def�򵥺ܶ�<br>
lambda ����ӵ���Լ��������ռ䣬�Ҳ��ܷ������в����б�֮���ȫ�������ռ���Ĳ�����

ð��ǰ�ǲ����������ж�����ö��Ÿ�����ð���ұߵķ���ֵ��<br>

```
sum = lambda arg1, arg2: arg1 + arg2
print("��Ӻ��ֵΪ��", sum(10, 20))
```

##### lambda���б��Ƶ�
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
>������
funcs��һ���б��б����ÿһ��Ԫ���Ǹ�lambda function��
Python�ıհ�(lambda��function��)�ᱣ�����������(i)��scoping(global)��������õ�ʱ��Ż�ȥ�Ҿ���Ķ���
��i����ͬ��ֵ���ڵ���ʱ��ȥȡ���µ�iֵ

##### ���ģ�
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
>������
�����lambda��һ���������������ÿ�δ���һ��Ĭ��ֵ�����Ĭ��ֵ��ÿ�ε�iָ��������funcs�б��е�
lambda��������һ��Ĭ��ֵ����������for i in data����˼

for i in data �ȼ��ڣ�
```
iterator = iter(data)
i = next(iterator)
# do something
i = next(iterator)
# do something
...
�� raise StopIteration
```