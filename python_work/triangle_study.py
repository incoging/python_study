# coding=utf-8
# 输出一个杨辉三角
# 方法一：利用推导列表


def triangles(line_num):

    # 用来控制输出行数
    n = 0
    line = [1]
    while n < line_num:
        print(line)
        line = line + [0]
        # L[-1]刚好取到L的最后一个元素
        line = [line[i - 1] + line[i] for i in range(len(line))]
        n += 1


# triangles(6)  # 调用triangles，打印出杨辉三角

# 方法二：利用生成器


def tri_yield(line_num):
    ret = [1]
    n = 0
    while n < line_num:
        yield ret
        pre = ret[:]
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        n += 1


gen = tri_yield(5)
# 打印输出gen这个生成器中的内容
for con in gen:
    print(con)

