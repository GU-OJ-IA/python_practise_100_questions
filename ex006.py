"""
Python 练习实例6:
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

实现方法：
逐个计算
"""

n = 100
f = list(range(n))
f[0] = 0
f[1] = 1
f[2] = 1

for i in range(3, n):
    f[i] = f[i - 1] + f[i - 2]

for i in f:
    print(i)