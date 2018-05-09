# 利用闭包返回一个计数器，每次调用它返回递增整数


def creater_counter():
    s = [0]
    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter


res = creater_counter()
print(res(), res(),res())
'''output:
1 2 3
'''
# 解释：
"""
因为整个过程只调用了一次creteCounter，就是counterA = createCounter(),
此时counterA得到的是createCounter内部返回的counter函数，以后每次counterA在执行的时候执行的都是counter()函数，
所以整个过程createCounter就只调用了一次，所以s也就只初始化了一次
另外：
若把函数中按照s = 0, s = s + 1, 是不行的。
因为内部函数不能修改外部变量
闭包的含义就是，调用内部函数，并且附带上外部变量
所以
s=0，s=s+1这种写法，每次调用内部函数，s都指向0这个数字对象
返回值就是1 1 1 1 1

然而写成 nonlocal s 或者 s=[0] 这两种情况时
前者把s声明成了非局部变量 
所以s=s+1就可以修改外部函数变量s的值
第一次调用，（内部函数，s=0），s+1,s=1,返回1
下一次调用，（内部函数，s=1），s+1,s=2,返回2
以此类推...
"""
