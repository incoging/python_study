# coding = utf-8
# 这个文档主要讲述去掉读入一行中的换行符
file = open()
for line in file.readlines():
    line = line.strip('\n')
