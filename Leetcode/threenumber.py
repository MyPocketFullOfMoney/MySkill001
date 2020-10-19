
# 时间：2020/10/8

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

      示例：给定数组 nums = [-1, 0, 1, 2, -1, -4]， 满足要求的三元组集合为：
         [
           [-1, 0, 1],
           [-1, -1, 2]
         ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List

class Solution:
    def threeSum(self,nums:List[int]) -> List[List[int]]:
        # 通过排序去重
        nums.sort()
        n = len(nums)
        ans = list()

        # 枚举a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c对应的指针，初始指向列表的最右端
            third = n - 1
            target = -nums[first]

            # 枚举b
            for second in range(first + 1,n):
                # 需要和上次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证b的指针在c的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着b的增加
                # 就不会有满足，a+b+c=0并且b<c的c了，所以可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


# main函数
if __name__ == '__main__':
    test = [-1, 0, 1, 2, -1, -4]
    demo = Solution()
    print('示例：[-1, 0, 1, 2, -1, -4]')
    print('输出：',demo.threeSum(test))