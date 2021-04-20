# coding=utf-8 Python 3.7.4
''' 
 * Description  : 两个数字相加
 * Author       : Lichongyou
 * Date         : 2020-07-23 20:05:08
 * LastEditTime : 2020-07-23 20:14:13
 * LastEditors  : Lichongyou
'''
while True:
    try:
        num_1 = float(input('请输入第一个数字：'))

        num_2 = float(input('请输入第二个数字：'))

        sum = num_1 + num_2
        print('两个数字的和：', sum)
        break
    except ValueError:
        print('你输入的不是数字！请重新输入！')
