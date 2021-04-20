# 递归实现斐波那契数列
# 时间：2020/10/17

# 定义函数
def recur_fibo(n):
    """ 递归函数
        输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-2) + recur_fibo(n-1))


# main函数
if __name__ == '__main__':
    # 获取用户输入
    nterms = int(input('请输入正整数：'))

    if nterms <= 0 :
        print('请输入正整数')
    else:
        print('斐波那契数列：')
        for i in range(nterms):
            print(recur_fibo(i))