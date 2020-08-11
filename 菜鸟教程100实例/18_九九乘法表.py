#coding=utf-8 Python 3.7.4
''' 
 * Description  : 9 * 9 乘法表
 * Author       : Lichongyou
 * Date         : 2020-08-04 16:43:47
 * LastEditTime : 2020-08-05 09:41:53
 * LastEditors  : Lichongyou
''' 

# 两个循环实现方式
for x in range(1,10):
    for y in range(1,x+1):
        print('{0}*{1}={2}'.format(x,y,x*y),end=' ')
    print(end='\n')
print('='*90)
# 列表推导
print('\n'.join('   '.join(['{}×{}={}'.format(i, j, i * j) for i in range(1, j + 1)]) for j in range(1, 10) )  )

