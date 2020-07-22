#coding=utf-8 Python 3.7.4
''' 
 * Description  : 常用的字典操作
 * Author       : Lichongyou
 * Date         : 2020-07-22 15:01:13
 * LastEditTime : 2020-07-22 16:25:30
 * LastEditors  : Lichongyou
''' 
dict_ori={'a':'1','b':'2','c':'3','d':'4'}
print('原始字典：',dict_ori)
#创建字典
dict={x:x+'+'+y for x,y in dict_ori.items()  }
print('加工后的字典：',dict)

#通过键名获取字典的值
print(dict['a'])

#使用get方法获取键值，可以设置默认值，不存在返回None
print('利用get方法获取\'a\'键名的键值：{0} \n利用不存在的键名\'e\'获取键值:{1}'.format( dict.get('a'),dict.get('e') ) )
print('dict[e]：',dict.get('e',0))

#修改元素
dict['a']='aaaa+1'
print('dict[a]：',dict)

#返回一个字典所有的Key
print(dict.keys())

#返回一个字典所有的value
print(dict.values())