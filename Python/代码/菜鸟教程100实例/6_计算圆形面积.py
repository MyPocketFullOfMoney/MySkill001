#coding=utf-8 Python 3.7.4
''' 
 * Description  : 计算圆形面积
 * Author       : Lichongyou
 * Date         : 2020-07-27 20:20:41
 * LastEditTime : 2020-07-27 20:43:05
 * LastEditors  : Lichongyou
''' 

#编写一个圆形类
class Circle :
    Pi = 3.142
    r = 0.0
    #定义构造函数
    def __init__(self, r):
        self.r = r
    
    def circle_area(self):
        return self.Pi * (self.r*self.r)

if __name__=='__main__':
    r = float(input('请输入圆的半径r：'))
    yuan = Circle(r)
    print('圆的面积为：',yuan.circle_area())