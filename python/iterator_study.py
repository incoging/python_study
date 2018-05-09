# 2.2.1 迭代器

"""
迭代器是一个实现了迭代器协议的容器对象，基于以下两个方法：
__next__: 返回容器的下一个元素
__iter__: 返回迭代器本身
"""

"""
迭代器遍历完序列时。会引发一个StopIteration异常，因此可以和循环兼容，后捕获这个异常结束循环。   
创建迭代器类:
"""
class CountDown:
    def __init__(self,step):
        self.step = step
    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        """Return the iterator itself."""
        return self

for elem in CountDown(4):
    print(elem)
"""
output:
3
2
1
0
"""