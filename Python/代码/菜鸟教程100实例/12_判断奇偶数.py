#coding=utf-8 Python 3.7.4
''' 
 * Description  : 判断奇偶数
 * Author       : Lichongyou
 * Date         : 2020-07-28 19:27:14
 * LastEditTime : 2020-07-28 19:32:21
 * LastEditors  : Lichongyou
''' 

while True:
    try:
        num = int(input('请输入一个正整数：'))
        if num <= 0:
            print('请输入一个正整数！')
            continue
        elif num % 2 == 0:
            print('{0}是偶数！',num)
        else:
            print('{0}是奇数！',num)
        # 退出循环
        break
    except ValueError:
        print('请输入一个正整数！')