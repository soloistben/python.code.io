# dict迭代

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:  # 只能查出key，不能查出value
    print(key)

for key,value in d.items():  #同时查出key&value
    print(key,value)


    
# list迭代

l = ['d', 'e', 'f']

for x in l:
    print(x)

for i, value in enumerate(l):  # enumerate函数可以把一个list变成索引-元素对
    print(i, value)


for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)		#在python，引用两个变量很常见
