"""
Python 练习实例4:
输入某年某月某日，判断这一天是这一年的第几天？

实现方法：
各月累加
"""

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date = input('输入某年某月某日（例如2019-8-12）：').split(sep='-')
year = int(date[0])
month = int(date[1])
day = int(date[2])

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    days_per_month[1] = 29

days_of_date = 0
if month == 1:
    days_of_date = day
else:
    for i in range(month - 1):
        days_of_date += days_per_month[i]

    days_of_date += day

print('共{}天'.format(days_of_date))
