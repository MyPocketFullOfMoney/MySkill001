#coding=utf-8 Python 3.7.4
''' 
 * Description  : 判断一个数字的正负
 * Author       : Lichongyou
 * Date         : 2020-07-28 14:31:20
 * LastEditTime : 2020-07-28 14:34:35
 * LastEditors  : Lichongyou
''' 

# 利用if .. elif .. else语句

# 用户输入数字
num = float(input('输入数字：'))

#判断
if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')