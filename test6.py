# 列表生成器

l = list(range(10))
print(l)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m+n for m in "ABC" for n in "123"]
print(L)

L = ['Hello','WWE','MIKE']	#假如含有数字和其他非字符串，lower()会出错
L = [l.lower() for l in L]
print(L)