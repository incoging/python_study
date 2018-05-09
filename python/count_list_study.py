# coding=utf-8
# 2017年9月6日14:34:38
# 统计一个列表中每个元素出现的次数。

# 方法一：
# from collections import Counter
#
# a = [2, 3, 4, 2, 3, 4, 5, 3, 5, 6, 8]
# result = Counter(a)
# print(result)
# '''
# Counter({3: 3, 2: 2, 4: 2, 5: 2, 6: 1, 8: 1})
# '''


# 方法二：
mylist = [1, 2, 3, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
myset = set(mylist)  # myset是另外一个列表，里面的内容是mylist里面的无重复 项
for item in myset:
    print("the %d has found %d" % (item, mylist.count(item)))
