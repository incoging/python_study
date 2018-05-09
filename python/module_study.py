def printHello():
    print("-" * 30)
    print("****** Hello ******")
    print("-" * 30)


if __name__ == '__main__':
    printHello()
    # __name__是python内置的一个变量，如果直接执行这个文件，__name__的值就等于__main__.
    # 如果是其他程序导入了这个模块，则那时这个模块对应的__name__就变成了模块名。参见module2
