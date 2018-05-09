# coding = utf-8

# lists = [[]] * 3
# print(lists)    #[[], [], []]
# lists[0].append(3)
# print(lists)    #[[3], [3], [3]]
# array = [0, 0, 0]
# matrix = [array] * 3
# matrix[0][1] = 1
# print(matrix)  #[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
# #即matrix = [array] * 3操作中，只是创建3个指向array的引用，所以一旦array改变，matrix中3个list也会随之改变。

lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists)
