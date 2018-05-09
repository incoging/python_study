# coding = utf-8

num = input("Please enter the length of the sequence: ")
num = int(num)

array = []
content = input("Please enter the array:")
content = content.split(" ")
for con in content:
    arr = int(con)
    array.append(arr)

value = []
for i in range(1, num + 1):
    for k in range(num):
        if k < i:
            sub_array = array[k:i]
            min = sub_array[0]
            sum = 0
            for j in range(len(sub_array)):
                if sub_array[j] < min:
                    min = sub_array[j]
                sum += sub_array[j]
            sub_value = min * sum
            value.append(sub_value)

max = value[0]
for index in range(len(value)):
    if value[index] > max:
        max = value[index]
print("The max equals to:", max)
