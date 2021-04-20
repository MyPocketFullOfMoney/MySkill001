'''
定义一个列表，并计算某个元素在列表中出现的次数
时间：2021/2/28
'''

# 利用list.count()的方法直接的出某元素的个数

list_example = [1,1,1,1,2,3,3,3,555,666,777,8,8]
num = 8
print('列表：',list_example)
print('统计元素{}在列表出现的次数'.format(num))
print('{0}出现{1}次!!!'.format(num,list_example.count(num)))