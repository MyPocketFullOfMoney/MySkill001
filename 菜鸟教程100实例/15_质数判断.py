#coding=utf-8 Python 3.7.4
''' 
 * Description  : 用户输入一个数字，判断是否为质数
 * Author       : Lichongyou
 * Date         : 2020-07-30 10:13:34
 * LastEditTime : 2020-07-30 10:32:25
 * LastEditors  : Lichongyou
''' 

''' for ... :
       语句
    else:
'''

#用户输入数字
num = int(input('请输入一个正整数：'))

#质数大于1
if num > 1:
    # 循环遍历
    for i in range(2,num):
        if(num%i == 0):
            print('{0}不是质数！'.format(num))
            print('{0}/{1}={3}',format(num,i,num/i))
            break
    else:
        print('{0}是质数！'.format(num))
else:
    print('{0}不是质数！'.format(num))