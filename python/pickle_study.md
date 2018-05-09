##### pickle 模块学习
Python提供的pickle模块可以序列化对象并保存到磁盘中，并在需要的时候读取出来，
几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化。
1. 将obj对象序列化存入已经打开的file中。
```
pickle.dump(obj, file, [,protocal])
# obj 想要序列化的对象
# file 目的文件名称路径
# protocol 序列化使用的协议，默认为0，如果为负值或者HIGHEST_PROTOCOL，则使用最高的协议版本。
```

2. 将file中的对象序列化读出。
```
pickle.load(file) # 读出file中的内容，并返回该对象
```

3. 将obj对象序列化为string形式，而不是存入文件中。
```
pickle.dumps(obj,[,protocol])
# obj 想要序列化的对象
# protocol 序列化使用的协议，默认为0，如果为负值或者HIGHEST_PROTOCOL，则使用最高的协议版本。
```

4. 从string中读出序列化前的obj对象。
```
pickle.loads(stirng)  # 从序列化后的string变量读出obj，并返回这个对象
```
> dump() 和 load() 与 dumps() 和 loads() 相比，还有另一种能力：
dump()函数能一个接着一个地将几个对象序列化存储到同一个文件中，
随后调用load()来以同样的顺序反序列化读出这些对象。

example：
```
# 导包
import pickle  

# 分别建立一个列表和一个字典
data_list = [[1, 1, 'yes'],  
            [1, 1, 'yes']]
data_dic = { 0: [1, 2, 3, 4], 1: ('a', 'b')}

# 以二进制形式打开文件
fw = open("./pickleTest.txt", 'wb')

# 将data_list序列化存入文件中
pickle.dump(data_list, fw, -1)

# 将data_dic序列化存入文件中, 使用默认协议
pickle.dump(data_dic, fw)

# 关闭文件
fw.close()


# 使用load()将数据从文件中序列化读出  
fr = open("./pickleTest.txt", 'rb')
data1 = pickle.load(fr)  
print(data1)  # [[1, 1, 'yes'], [1, 1, 'yes']]
data2 = pickle.load(fr)  
print(data2)   # {0: [1, 2, 3, 4], 1: ('a', 'b')}
fr.close()  


#使用dumps()和loads()举例  
p = pickle.dumps(dataList)  
print( pickle.loads(p) )  # [[1, 1, 'yes'], [1, 1, 'yes']]
p = pickle.dumps(dataDic)  
print( pickle.loads(p) )  # {0: [1, 2, 3, 4], 1: ('a', 'b')}
```