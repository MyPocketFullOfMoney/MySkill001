#coding=utf-8 Python 3.7.4
''' 
 * Description  : 阿姆斯特朗数
 * Author       : Lichongyou
 * Date         : 2020-08-05 09:50:50
 * LastEditTime : 2020-08-06 11:27:41
 * LastEditors  : Lichongyou
''' 

# 阿姆斯特朗数的定义：一n位正整数=各位数字n次方之和
# 举例：1^3 + 5^3 + 3^3 = 153

# 获取用户输入
num = int( input('请输入一个正整数：') )

sum = 0

# 转换为字符串，计算长度(指数)
n = len( str(num) )

temp = num
# 检测
while(temp>0):
    # 每次都取出个位
    digit = temp % 10
    # 求和
    sum += digit**n
    # 整除，商，向下取整
    temp //= 10
# 输出结果
if (num == sum):
    print('{0}是阿姆斯特朗数！'.format(num))
else:
    print('{0}不是阿姆斯特朗数！'.format(num))