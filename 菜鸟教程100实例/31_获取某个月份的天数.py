# 利用Python的Calendar模块来计算每个月的天数
# 时间：2020/10/27

import calendar

'''
输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
以上实例输出的意思为 2020 年 10 月份的第一天是星期四，该月总共有 31 天
'''

print('Python模块：',calendar.monthrange(2020,10))

# 函数实现
def mon_days(year:int,month:int) -> int:
    # 列表下标从1开始,表示每个月份的天数，闰年2月除外
    mdays = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if 1 <= month <=12 :
        ndays = mdays[month] + (month == 2 and calendar.isleap(year))
        return ndays

print('自定义函数：',mon_days(2000,2))
