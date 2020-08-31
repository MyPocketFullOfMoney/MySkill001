#coding=utf-8 Python 3.7.4
''' 
 * Description  : 通过Python内部函数，对用户输入的数字进行进制转换
 * Author       : Lichongyou
 * Date         : 2020-08-11 22:00:49
 * LastEditTime : 2020-08-11 22:04:31
 * LastEditors  : Lichongyou
''' 

num = int(input('输入数字：'))

# 输出二进制
print('{0}的二进制表示：{1}'.format(num,bin(num)))