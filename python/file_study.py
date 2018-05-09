# coding = utf-8
# 逐行读取txt文件内容的方法

# 方法一
f = open("foo.txt")             # 返回一个文件对象
line = f.readline()              # 调用文件的 readline()方法
while line:
    print(line,)                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()

f.close()

# 方法二
for line in open("foo.txt"):
    print(line,)                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用


# 方法三
f = open("c:\\1.txt", "r")
lines = f.readlines()            # 读取全部内容
for line in lines:
    print(line)
f.close()

# 光标返回
# 调用read函数，读到哪，那么光标的位置就会留在哪里
# 使用f.tell()函数可以返回光标所在的位置。tell()函数是按照字符来计算的

# 光标操作
'''
f.seek(0) 即将光标的位置定位到文件的开头，也可以是其他参数，10，20等
'''

#python保存numpy数据：
# np.savetxt("result.txt", numpy_data)

#保存list数据：
# file=open('data.txt','w')
# file.write(str(list_data))
# file.close()

# file.writelines(lists) 是不换行的写入，可用以下方法在写入时换行。
# 方法一：
# for line in lists:
#     file.write(line+'\n')
#
# # 方法二：
# lists=[line+"\n" for line in lists]
# file.writelines(lists)
#
# # 方法三：
# file.write('\n'.join(lists))