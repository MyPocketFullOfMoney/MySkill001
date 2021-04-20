#coding=utf-8 Python 3.7.4
''' 
 * Description  : 摄氏温度转华氏温度
 * Author       : Lichongyou
 * Date         : 2020-07-28 11:38:10
 * LastEditTime : 2020-07-28 11:47:13
 * LastEditors  : Lichongyou
''' 

# 公式：华氏度 = 32°F+ 摄氏度 × 1.8
# 公式：摄氏度 = (华氏度 - 32°F) ÷ 1.8

# 接受用户输入
celsius = float(input('输入摄氏温度：'))

# 计算华氏温度
fahrenheit = 32 + (celsius*1.8)

print('{0}摄氏度转换为华氏温度：{1}'.format(celsius,fahrenheit))