# 通过datetime模块获取昨天日期
# 2020/10/30

import datetime

def getYesterday():
    # 获取今天日期
    today = datetime.date.today()
    #
    oneday = datetime.timedelta(days=1)

    yesterday = today - oneday
    return yesterday


print(getYesterday())