# conding = utf-8
input_num = input("请输入一个整数：")
length = len(input_num)
record = []
new_num = []

dic = {}

# 先把最终要得到的序列全部置为a
for index in range(length):
    new_num.append("a")

# 找出所有的重复数字，并标记出位置
for i in range(length):
    st = input_num[i]
    for j in range(length):
        # if st == input_num[j]:
        #     dic[i] = input_num[i]
        if st == input_num[j] and (i != j):
            dic[i] = input_num[i]
            record.append(i)
            break
# print(dic)

# 把不重复的数字加入到最终的那个序列
print(record)
# print(new_num)
for k in range(length):
    if k not in record:
        new_num[k] = input_num[k]


def findnum(start):
    first_num = 0
    for i in range(start, length):
        if ord(new_num[i]) != 97:
            first_num = i
            break
    return first_num


# 从左边最高位开始，与现有的new_num中除这一位的最高位比较
for i in range(len(record)):
    if record[i] != None:
        first_num_loc = findnum(record[i] + 1)
        if input_num[record[i]] > input_num[first_num_loc]:
            for key, value in dic.items():
                if value == input_num[record[i]]:
                    new_num[record[i]] = 'a'
            new_num[record[i]] = input_num[record[i]]
        else:
            isthat = False
            for index in range(first_num_loc, length):
                if input_num[index] == input_num[record[i]]:
                    isthat = True
            if isthat == True:
                for key, value in dic.items():
                    if value == input_num[record[i]] and key < first_num_loc:
                        new_num[record[i]] = 'a'
                        for key, value in dic.items():
                            if value == input_num[record[i]]:
                                new_num[record[i]] = input_num[record[i]]
                                break
                        for key, value in dic.items():
                            if value == input_num[record[i]]:
                                new_num[record[i]] = 'a'
            else:
                rec = record[i]
                for key, value in dic.items():
                    if value == input_num[record[i]]:
                        new_num[record[i]] = input_num[record[i]]
                        break
                w = 0
                for key, value in dic.items():
                    for q in range(w, len(record)):
                        b = input_num[rec]
                        if value == input_num[rec]:
                            record[q] = None
                            w = q + 1
                            break

print(new_num)
