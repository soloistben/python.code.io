# -*- coding: utf-8 -*-
from functools import reduce
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    # 一段字符，第一个单词的首字母大写
    # return str(name).capitalize()
    # return str(name)[0: 1].upper() + str(name)[1:].lower()
    # 一段字符，每个单词的首字母大写
    return str(name).title()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def product(x, y):
        return x * y
    return reduce(product, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))