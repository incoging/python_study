# coding = utf-8
# 列表切割
list = [1, 3, 5, 6, 7, 8, 9, 2, 3]

# list[start:end:step] #相当于从下标的0 到end-1
list1 = list[0:3]
print(list1)  # [1, 3, 5]

# 若从头开始切割，那么可以忽略start位的0.eg：list[:3]
list2 = list[:3]
print(list2)  # [1, 3, 5]

# 若一直切割到列表的尾部，则可以忽略end位，eg：list[5:]
list3 = list[5:]
print(list3)  # [8, 9, 2, 3]

# 索引留空时，会生成一份原列表的拷贝，并且切割列表时不会改变原列表
list4 = list[:]
print(list4)  # [1, 3, 5, 6, 7, 8, 9, 2, 3]

assert list4 == list and list4 is not list  # true
