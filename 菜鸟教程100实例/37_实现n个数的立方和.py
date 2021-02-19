# 计算n个数的立方和
# 时间：2021/2/19
'''
例子
输入 : n = 5

输出 : 225

公式 : 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225

'''

# 定义立方和函数
def sumOfSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i*i
    return sum

if __name__ == "__main__":
    # 调用函数
    n = 5
    print('1-5的立方和：',sumOfSeries(n))