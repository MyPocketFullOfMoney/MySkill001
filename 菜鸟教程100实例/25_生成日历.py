# 利用Python自带的日历模块生成日历
# 时间：2020/10/14

# 引入日历模块
import calendar

# 输入指定的年月
yy = int(input('输入年份：'))
mm = int(input('输入月份：'))
# 打印日历
print(calendar.month(yy,mm))