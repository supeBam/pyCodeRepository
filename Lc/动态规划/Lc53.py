from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 正数一定选、负数和0 则重新开始
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([5,4,-1,7,8]))