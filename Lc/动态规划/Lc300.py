import collections
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        起始  f(0) = 1
        转移方程： 当 nums[i] > nums[0, j] j < i  max(f(i), f(j) + 1)
        '''

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # 双指针，二分法
    def lengthOfLIS2(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0

        for num in nums:
            # 每次枚举
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                # 往mid后面找
                if tails[m] < num:
                    i = m + 1
                # 往前面找
                else:
                    j = m
            # 修改值，
            tails[i] = num
            # 如果 num 比之前的值大，则 右指针又移动（只有当 tails[m] >= num的时候才会 移动右指针）
            if j == res:
                res += 1


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS2([5, 10, 12, 8, 6, 9]))
