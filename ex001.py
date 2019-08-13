"""
Python 练习实例1:
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

实现方法：
利用set中元素互不相同的特性，去除重复的数字
"""

nums = set()

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i == j or i == k or j == k:
                continue

            num = i * 100 + j * 10 + k
            nums.add(num)

print('共有{}个数字'.format(len(nums)))

for num in nums:
    print(num)
