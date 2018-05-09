# 一行代码实现99乘法表

print("\n".join("\t".join(["%s*%s=%s" % (x, y, x * y) for y in range(1, x + 1)]) for x in range(1, 10)))
# 注意，这里的两个列表推导是嵌套的，不是平行的，外层的x循环嵌套里层的y循环
