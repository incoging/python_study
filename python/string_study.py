
# str.strip()
"""
 strip() 方法用于移除字符串头尾指定的字符（默认为空白字符，包括Tab，空格，换行符）。
"""
str = "0000000     Runoob  0000000"
print(str.strip('0'))  # 去除首尾字符 0

str2 = "   Runoob      \n"
# print(str2.strip())   # 去除首尾空格，及换行符
print("-----")