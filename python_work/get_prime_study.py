# 求出2到100的素数

# 方法一：
# num_list = [x for x in range(2, 101)]
# re = []
#
#
# def get_prime(the_list):
#     fir = the_list[0]
#     re.append(fir)
#
#     def prime(x):
#         return x % fir != 0
#
#     new_list = list(filter(prime, the_list[1:]))
#     if len(new_list) > 1:
#         re_t = get_prime(new_list)
#         return re_t  # 如果这里不加return， 那么就相当于只有最里层的get_prime有返回值，从倒数第二层到最外层都没有返回值
#         # 所以这里加上return，一层一层的返回的时候，每一层都是有返回值的
#     else:
#         re.extend(new_list)
#         return re
#
#
# res = get_prime(num_list)
# print(res)


# 方法二：
# 构造一个从3开始的奇数数列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0  # 如果x不能整除n，那么返回True


# 定义一个生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break