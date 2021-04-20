#coding=utf-8 Python 3.7.4
''' 
 * Description  : 涉及元组的主要概念和操作
 * Author       : Lichongyou
 * Date         : 2020-07-22 11:12:31
 * LastEditTime : 2020-07-22 15:00:17
 * LastEditors  : Lichongyou
''' 

#创建一个元组

tup=( i for i in range(10) )
#元组推导式得到的是一个生成器
print('元组生成器：',tup)
#输出利用tuple函数转换或者使用for循环遍历生成器
print('元组:',tuple(tup))

#for循环遍历,访问过生成器对象后，生成器对象已经不存在
for i in tup:
    #输出为空
    print(i,end=' ')
print('内存ID：',id(tup))
#所谓元组的不可变指的是元组所指向的内存中的内容不可变。元组元素不可修改。
tup=(1,2,3)
print('内存ID：',id(tup))
print(tup)

dict={'1':'0'}
