# coding=utf-8
# 这个文档用来记录如何调用另一个Python文件中的代码

# 1、在同一文件目录下
'''
b.py和a.py在同一文件目录下，要使用a中的func(),则通过如下命令即可调用：
import a   #引用模块
a.func()
或：
from a import func   #这里确实是不需要()的
func()     #这种引用模式就不再需要加上模块名的前缀了
'''

# 2、不同文件目录下
'''
若不在同一目录，python查找不到，必须进行查找路径的设置，将模块所在的文件夹加入系统查找路径
import sys
sys.path.append("a.py所在的路径")
import a
a.func()
'''
