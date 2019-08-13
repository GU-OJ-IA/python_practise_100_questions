"""
Python 练习实例5:
输入三个整数x,y,z，请把这三个数由小到大输出

实现方法：
if语句分情况判断
"""

nums = input('输入三个数字（例如1,2,3）：').split(sep=',')
xyz = []
for num in nums:
    xyz.append(int(num))
xyz.sort()

print(xyz)
