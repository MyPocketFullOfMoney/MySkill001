#coding=utf-8 Python 3.7.4
''' 
 * Description  : Python交换变量不需要使用临时变量
 * Author       : Lichongyou
 * Date         : 2020-07-28 14:21:08
 * LastEditTime : 2020-07-28 14:26:53
 * LastEditors  : Lichongyou
''' 

#用户输入两个数
x = int(input('请输入变量x：'))
y = int(input('请输入变量y：'))

print('交换前x={0},y={1}'.format(x,y))
#交换变量
x,y = y,x
print('交换后x={0},y={1}'.format(x,y))