# 给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。
# 返回使字符串任意相邻两个字母不相同的最小删除成本。
# 时间：2020/10/15
# 使用'贪心'算法得思想，即保留重复字符中删除代价最大的
'''
示例：
输入：s = "abaac", cost = [1,2,3,4,5]
输出：3
解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-deletion-cost-to-avoid-repeating-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def minCost(self,s:str,cost:List[int]) -> int:
        i = 0
        length = len(s)
        res = 0
        # 遍历字符串
        while i < length:
            ch = s[i]
            MaxValue = 0
            total = 0
            # 寻找重复字符中删除代价最大的
            while i < length and s[i] == ch:
                MaxValue = max(MaxValue,cost[i])
                total += cost[i]
                i +=1
            res += (total - MaxValue)
        return res

if __name__ == '__main__':
    test_str = 'abaac'
    test_cost = [1,2,3,4,5]
    demo = Solution()
    print('删除最小代价为：',demo.minCost(test_str,test_cost))