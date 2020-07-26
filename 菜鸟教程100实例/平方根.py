#coding=utf-8 Python 3.7.4
''' 
 * Description  : 计算一个数字的平方根
 * Author       : Lichongyou
 * Date         : 2020-07-26 12:30:25
 * LastEditTime : 2020-07-26 12:37:34
 * LastEditors  : Lichongyou
''' 

# 利用python的特殊符号：**
# x ** y表示：x的y次方;那么求平方根， x ** 0.5
# 但该程序只适用于求解正数的平方根，无法求解负数、复数的平方根

x = float(input('请输入一个数字：'))

print('该数的平方根为：',x ** 0.5)