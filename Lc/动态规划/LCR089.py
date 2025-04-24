from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        起始值：f(0) = nums[0]
        转移方程：
        f(n) = f(n-2) + nums[n]
        max(f(n), f(n-1))

        '''
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1],  dp[i - 2] + nums[i])

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
