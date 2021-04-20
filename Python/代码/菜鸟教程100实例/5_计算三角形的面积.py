#coding=utf-8 Python 3.7.4
''' 
 * Description  : 根据三角形三边的长度，计算三角形面积
 * Author       : Lichongyou
 * Date         : 2020-07-27 14:44:38
 * LastEditTime : 2020-07-27 15:05:39
 * LastEditors  : Lichongyou
''' 

while True:
    try:
        a = float(input('输入三角形的第一边长：'))
        b = float(input('输入三角形的第二边长：'))
        c = float(input('输入三角形的第三边长：'))

        #判断能否构造三角形
        if(a+b>c and a+c>b and b+c>a):
            #计算半周长
            s = (a + b + c) / 2
            #计算面积
            area = (s*(s-a)*(s-b)*(s-c) ) ** 0.5
            print('三角形的面积：',area)
            break
        else:
            print('输入的三边无法构成三角形！请重新输入！')

    except ValueError:
        print('请输入正确的边长！')