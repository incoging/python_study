# 利用filter查找回数，即从左向右和从右向左读都是一样的数，eg：12321, 989

# 定义一个判断是否为回文数字函数，是返回True, 否则返回False
def is_palindrome(n):
    a = str(n)
    return a == a[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))