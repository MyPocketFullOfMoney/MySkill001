#coding=utf-8 Python 3.7.4
''' 
 * Description  : 用户输入一个正整数，程序计算该数得阶乘！
 * Author       : Lichongyou
 * Date         : 2020-08-03 11:35:32
 * LastEditTime : 2020-08-04 16:41:28
 * LastEditors  : Lichongyou
''' 

# 通过循环实现
def for_factorial(n:int) -> int  :
    ''' 
     * description: 计算一个数字的阶乘！
     * n {int} 
     * return: n的阶乘
    ''' 
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum
# 递归实现
def factorial(n):
    if n < 0:
        return ('输入错误！')
        
    elif n == 1 :
        return 1

    else :
        return n * factorial(n-1)



if __name__ == '__main__':
    num = int(input('请输入一个正整数：'))
    
    if num > 0 :
        sum = for_factorial(num)
        print('{0}!的阶乘：{1}'.format(num,sum) )
        print('递归实现：',factorial(num))