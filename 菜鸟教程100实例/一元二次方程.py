#coding=utf-8 Python 3.7.4
''' 
 * Description  : 利用一元二次方程求根公式，求解
 * Author       : Lichongyou
 * Date         : 2020-07-26 12:46:58
 * LastEditTime : 2020-07-26 13:12:47
 * LastEditors  : Lichongyou
''' 

# 二次方程： aX**2 + bX + c = 0
# 其中a,b,c用户提供，且a ≠ 0
# 求根公式 x = [ -b ± ( b**2 - 4ac )**0.5 ] / 2a

# 导入cmath复杂数学运算模块
import cmath

while True:
    a = float(input('请输入实数a：'))
    if a == 0:
        print('实数a不能等于0，请重新输入!')
        continue
    break


b = float(input('请输入实数b：'))
c = float(input('请输入实数c：'))
#输出一元二次方程
print('一元二次方程：{0}x**2 + {1}x + {2}'.format(a,b,c))
#计算( b**2 - 4ac )
d = b**2 - (4*a*c)

# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
 
print('结果为 {0} 和 {1}'.format(sol1,sol2))