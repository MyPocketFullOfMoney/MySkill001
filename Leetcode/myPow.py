# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 时间：2020/10/14
# 快速幂法 时间复杂度：O(log n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        # 对指数n进行判断，n < 0 转换为(1/x)的-n次方
        if n < 0:
            x , n = 1 / x , -n
        # 循环
        while n:
            if n & 1 :
                res *= x
            x *= x
            n >>= 1
        return res

if __name__ == '__main__':
    demo = Solution()
    x = int(input('输入整数x:'))
    n = int(input('输入指数n:'))
    print('结果：',demo.myPow(x,n))