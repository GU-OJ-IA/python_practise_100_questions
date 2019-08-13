"""
Python 练习实例3：
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

实现方法：
逐个试凑
"""

from math import sqrt

nums = range(100000)
results = []

for num in nums:
    if sqrt(num + 100).is_integer() and sqrt(num + 100 + 168).is_integer():
        results.append(num)

for num in results:
    print(num)
