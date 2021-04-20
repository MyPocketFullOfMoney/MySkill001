#coding=utf-8 Python 3.7.4
''' 
 * Description  : 用户给出指定范围，寻找范围内的所有素数
 * Author       : Lichongyou
 * Date         : 2020-07-28 20:16:25
 * LastEditTime : 2020-07-28 20:27:16
 * LastEditors  : Lichongyou
''' 

# 用户指定范围
lower = int(input('输入区间最小值：'))
upper = int(input('输入区间最大值：'))

# 判断输入的区间是否合理
if lower <= upper:
    # 遍历求解
    for num in range(lower,upper+1):
        # 素数大于1
        if num > 1:
            for i in range(2,num):
                if(num%2 == 0):
                    break
            else:
                print(num,end=' ')
        else:
            print('素数大于1！')
else:
    print('输入错误！程序退出！')