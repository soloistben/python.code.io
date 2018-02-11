# 类似函数重写（设置默认参数）
# 设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）;
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。


def power(x):  # 求平方
    return x * x


def power(x, n=2):  # 求n次方(默认n=2)
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
print(power(5))
print(power(5, 3))


def add_list(L=[]):  # 默认参数为一个空的list，在函数中添加一个字符串
    L.append('END')
    return L

print(add_list([1, 2, 3]))  # [1, 2, 3, 'END']
print(add_list())  # ['END']
print(add_list())  # 多次打印函数中的默认值['END', 'END']


def add_list(L=None):  # 默认参数变成一个变量，None是不变对象
                       # 不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
    if L is None:
        L = []

    L.append('END')
    return L
print(add_list())  # ['END']
print(add_list())  # ['END']
