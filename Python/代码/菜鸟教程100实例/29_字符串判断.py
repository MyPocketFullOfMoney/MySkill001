# 利用Python内置函数判断字符串
# 时间：2020/10/19

# 测试实例一
print('测试实例一')
str = 'runoob.com'
print('字符串：',str)
print('判断所有字符都是数字或者是字母:',str.isalnum())
print('判断所有字符都是字母：',str.isalpha())
print('判断所有字符都是数字：',str.isdigit())
print('判断所有字符都是小写：',str.islower())
print('判断所有字符都是大写：',str.isupper())
print('判断所有字符都是首字母大写：',str.istitle()) # 像标题
print('判断所有字符都是空白字符：',str.isspace()) #、\t、\n、\r

print('='*50)
print('测试实例二')
str = 'runoob'
print('字符串：',str)
print('判断所有字符都是数字或者是字母:',str.isalnum())
print('判断所有字符都是字母：',str.isalpha())
print('判断所有字符都是数字：',str.isdigit())
print('判断所有字符都是小写：',str.islower())
print('判断所有字符都是大写：',str.isupper())
print('判断所有字符都是首字母大写：',str.istitle()) # 像标题
print('判断所有字符都是空白字符：',str.isspace()) #、\t、\n、\r