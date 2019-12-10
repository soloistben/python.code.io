#可变参数
#数学题为例子，给定一组数字a，b，c……，请计算a^2 + b^2 + c^2 + ……。

def calc(number):	#参数为 list or tuple,每次输入参数则都需要在参数新构造  list or tuple
	sum = 0
	for n in number:
		sum += n*n
	return sum

print(calc([1,2,3]))	#list[1,2,3]	序列（允许修改）
print(calc((1,2,3)))	#tuple(1,2,3)	元组（不允许 修改or删除 元组中的元素）

def calc(*number):	#参数是可变，参数每次输入参数则都需要在参数不需要构造  list or tuple
	sum = 0
	for n in number:
		sum += n*n
	return sum

print(calc(1,2,3))