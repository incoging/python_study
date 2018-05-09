# coding = utf-8

# 正则表达式
# re.match函数尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
import re

print(re.match("www", "www.baidu.com").span())
print("我叫%s, 今年%d岁。" % ("小明", 10))
