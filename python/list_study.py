# coding = utf-8

# lists = [[]] * 3
# print(lists)    #[[], [], []]
# lists[0].append(3)
# print(lists)    #[[3], [3], [3]]
# array = [0, 0, 0]
# matrix = [array] * 3
# matrix[0][1] = 1
# print(matrix)  #[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
# #��matrix = [array] * 3�����У�ֻ�Ǵ���3��ָ��array�����ã�����һ��array�ı䣬matrix��3��listҲ����֮�ı䡣

lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists)
