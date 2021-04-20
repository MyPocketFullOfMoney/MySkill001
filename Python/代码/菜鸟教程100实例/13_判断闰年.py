#coding=utf-8 Python 3.7.4
''' 
 * Description  : 判断用户输入的年份是否为闰年！
 * Author       : Lichongyou
 * Date         : 2020-07-28 20:39:38
 * LastEditTime : 2020-07-28 21:01:20
 * LastEditors  : Lichongyou
''' 

# 定义函数
def is_leap_year(year:int):
    # 能被4整除为闰年;当是整百年时，需要能被400整除！
    if year%4 == 0:    
        # 判断是否为整百年
        if year%100 == 0 :
            if year%400 == 0:
                print('{0}是闰年！'.format(year))
            else:
                print('{0}不是闰年！'.format(year))
        else:
            print('{0}是闰年！'.format(year))
    else:
        print('{0}不是闰年！'.format(year))

if __name__ == "__main__":
    try:
        year = int(input('请输入一个年份：'))
        if year > 0:
            is_leap_year(year)
        else:
            print('输入错误！退出！')
    except:
        print('输入错误！退出！')
