class Solution:
    def fib(self, n: int) -> int:

        i,j = 0,1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        for _ in range(n-1):
            j,i = i+j,j

        return j%1000000007