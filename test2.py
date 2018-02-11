# 尝试导入.py文件中的自定义函数
from abs_test import my_abs
import math
print(my_abs(99 - 1000))

# 游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值
t = move(100, 100, 60, math.pi / 6)
print(t)  # 返回值是一个tuple
