"""
移除字符串中指定位置的字符
时间：2021/3/15
"""

test_str = 'Python'
mov_num = 2
new_str = ''
print('原始字符串：',test_str)

"""遍历字符串，重新拼接"""
for str_n in range(0,len(test_str)):
    
    if str_n != mov_num:
        new_str = new_str + test_str[str_n]
print('移除后的字符串：',new_str)

"""利用replace函数替换字符串中的字符"""
new_str2 = test_str.replace(test_str[mov_num],'',1)
print('利用replace函数替换：',new_str2)