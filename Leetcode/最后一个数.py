class Solution:
    def lastRemaining(self, n: int, m: int) -> int:

        nums = [x for x in range(n)]
        
        count = 1
        while nums:
            
            if len(nums) == 1: return nums[0]
            
            for i in nums:
                if count == m:
                    nums.remove(i)
                    count = 1
                else:
                    count += 1

if __name__ == '__main__':
    test = Solution()
    test.lastRemaining(5,3)