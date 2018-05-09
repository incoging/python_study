# coding = utf-8
def clock():
    n1 = input("请输入现在的指针情况：")
    n2 = input("请输入要旋转的正确位置：")
    n1 = int(n1)
    n2 = int(n2)

    if abs(n1 - n2) > 180:
        # print(360 - n1 + n2)
        if n1 > n2:
            print(360 - n1 + n2)
        elif n2 > n1:
            print(-(360 - n2 + n1))
    else:
        print(n2 - n1)


if __name__ == "__main__":
    clock()
