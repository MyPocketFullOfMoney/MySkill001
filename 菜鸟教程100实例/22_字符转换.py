#coding=utf-8 Python 3.7.4
''' 
 * Description  : 字符和ASCII码之间的转换
 * Author       : Lichongyou
 * Date         : 2020-08-31 09:31:08
 * LastEditTime : 2020-08-31 09:44:27
 * LastEditors  : Lichongyou
''' 
 # 用户输入字符
chr_1 = input('请输入一个字符：')
 # 用户输入ASCII码，并转换为整型
asc_1 = int(input('请输入一个ASCII码：'))

print(chr_1,'的ASCII码为',ord(chr_1))
print(asc_1,'的字符为',chr(asc_1))
