## collectionsģ��
collectionsģ����Python 2.4�汾��ʼ�����룬������dict��set��list��tuple�����һЩ������������ͣ��ֱ��ǣ�

* OrderedDict�ࣺ�����ֵ䣬���ֵ�����ࡣ������2.7��
* namedtuple()����������Ԫ�飬��һ������������������2.6��
* Counter�ࣺΪhashable������������ֵ�����ࡣ������2.7��
* deque��˫����С�������2.4��
* defaultdict��ʹ�ù������������ֵ䣬ʹ���ÿ���ȱʧ���ֵ����������2.5

### Counter��
Counter���Ŀ������������ֵ���ֵĴ���������һ��������������ͣ����ֵ�ļ�ֵ����ʽ�洢��
����Ԫ����Ϊkey���������Ϊvalue������ֵ�����������Interger������0�͸�������
Counter����������Ե�bags��multisets�����ơ�

##### ����

```
>>> c = Counter()  # ����һ���յ�Counter��
>>> c = Counter('gallahad')  # ��һ����iterable����list��tuple��dict���ַ����ȣ�����
>>> c = Counter({'a': 4, 'b': 2})  # ��һ���ֵ���󴴽�
>>> c = Counter(a=4, b=2)  # ��һ���ֵ�Դ���
```

##### ����ֵ�ķ�����ȱʧ�ļ�

�������ʵļ�������ʱ������0��������KeyError�����򷵻����ļ�����

```
>>> c = Counter("abcdefgab")
>>> c["a"]
2
>>> c["c"]
1
>>> c["h"]
0
```

##### �������ĸ��£�update��subtract��

����ʹ��һ��iterable���������һ��Counter���������¼�ֵ��
�������ĸ��°������Ӻͼ������֡����У�����ʹ��update()������

```
>>> c = Counter('which')
>>> c.update('witch')  # ʹ����һ��iterable�������
>>> c['h']
3
>>> d = Counter('watch')
>>> c.update(d)  # ʹ����һ��Counter�������
>>> c['h']
4
```

������ʹ��subtract()������

```
>>> c = Counter('which')
>>> c.subtract('witch')  # ʹ����һ��iterable�������
>>> c['h']
1
>>> d = Counter('watch')
>>> c.subtract(d)  # ʹ����һ��Counter�������
>>> c['a']
-1
```
##### ����ɾ��

������ֵΪ0ʱ��������ζ��Ԫ�ر�ɾ����ɾ��Ԫ��Ӧ��ʹ��del��

```
>>> c = Counter("abcdcba")
>>> c
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
>>> c["b"] = 0
>>> c
Counter({'a': 2, 'c': 2, 'd': 1, 'b': 0})
>>> del c["a"]
>>> c
Counter({'c': 2, 'b': 2, 'd': 1})
```

##### elements()

����һ����������Ԫ�ر��ظ��˶��ٴΣ��ڸõ������оͰ������ٸ���Ԫ�ء�
Ԫ��������ȷ��˳�򣬸���С��1��Ԫ�ز���������

```
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
```

##### most_common([n])

����һ��Top-N�б����nû�б�ָ�����򷵻�����Ԫ�ء������Ԫ�ؼ���ֵ��ͬʱ����������ȷ��˳��ġ�

```
>>> c = Counter('abracadabra')
>>> c.most_common()
[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
>>> c.most_common(3)
[('a', 5), ('r', 2), ('b', 2)]
```

##### ǳ����copy

```
>>> c = Counter("abcdcba")
>>> c
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
>>> d = c.copy()
>>> d
Counter({'a': 2, 'c': 2, 'b': 2, 'd': 1})
```

##### �����ͼ��ϲ���

+��-��&��| ����Ҳ��������Counter������&��|�����ֱ𷵻�����Counter�����Ԫ�ص���Сֵ�����ֵ��
��Ҫע����ǣ��õ���Counter����ɾ��С��1��Ԫ�ء�

```
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d  # c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d  # subtract��ֻ��������������Ԫ�أ�
Counter({'a': 2})
>>> c & d  # ����:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
>>> c | d  # ����:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
```

##### ��������

```
sum(c.values())     # ���м���������
c.clear()           # ����Counter����ע�ⲻ��ɾ��
list(c)             # ��c�еļ�תΪ�б�
set(c)              # ��c�еļ�תΪset
dict(c)             # ��c�еļ�ֵ��תΪ�ֵ�
c.items()           # תΪ(elem, cnt)��ʽ���б�
Counter(dict(list_of_pairs))         # ��(elem, cnt)��ʽ���б�ת��ΪCounter�����
c.most_common()[:-n:-1]              # ȡ���������ٵ�n-1��Ԫ��
c += Counter()                       # �Ƴ�0�͸�ֵ
```
