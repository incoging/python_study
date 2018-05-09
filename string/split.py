# coding = utf-8
# split()函数
# 语法：str.split(str="",num=string.count(str))[n]
# 参数说明：
# str：   表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
# num：表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
# [n]：   表示选取第n个分片

# 使用默认分隔符
# u1 = "www.baidu.com"
# print(u1.split())            #['www.baidu.com']


# 以"."为分隔符
# u2 = "www.taobao.com"
# print(u2.split("."))        #['www', 'taobao', 'com']


# 分割0次
# con =  u2.split('.', 0)
# print(con)                 #['www.taobao.com']


# # 分割一次
# con =  u2.split('.', 1)
# print(con)                 #['www', 'taobao.com']


# # 分割两次
# con = u2.split('.', 2)
# print(con)                   #['www', 'taobao', 'com']


# # 分割两次，并取序列为1的项
# con = u2.split('.', 2)[1]
# print(con)                     #taobao


# # 分割最多次（实际与不加num参数相同）
# con = u2.split('.', -1)
# print(con)                      #['www', 'taobao', 'com']
#
#
# # 分割两次，并把分割后的三个部分保存到三个变量
# u1, u2, u3 = u2.split('.', 2)
# print(u1)             #www
# print(u2)             #taobao
# print(u3)             #com



# 去掉换行符

# c = '''say
# hello
# baby'''
# print(c)         #say
# hello
# baby
# con = c.split("\n")
# print(con)                # ['say', 'hello', 'baby']



# 分离文件名和路径
import os

# con = os.path.split('/dodo/soft/python/')
# print(con)              #('/dodo/soft/python', '')

con = os.path.split('/dodo/soft/python')  # 注意与上面相比少了一个"/"
print(con)  # ('/dodo/soft', 'python')



# 一个超级好的例子
#
# str = "hello boy<[www.doiido.com]>byebye"
# con = str.split("[")[1].split("]")[0]
# print(con)              # www.doiido.com


# con = str.split("[")[1].split("]")[0].split(".")
# print(con)          # ['www', 'doiido', 'com']

print("abc")
