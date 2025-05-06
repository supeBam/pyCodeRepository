import collections
from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        maxValue = max(nums)
        indexSum = [0] * (maxValue + 1)

        for num in nums:
            indexSum[num] += num

        # 打家劫舍
        dp = [0] * (maxValue + 1)
        for i in range(len(indexSum)):
            dp[i] = max(dp[i - 1], dp[i - 2] + indexSum[i])

        return dp[-1]

    # 优化，改为变量
    def deleteAndEarn2(self, nums: List[int]) -> int:
        maxValue = max(nums)
        indexSum = [0] * (maxValue + 1)

        for num in nums:
            indexSum[num] += num

        # 打家劫舍
        a, b = indexSum[0], 0
        for i in range(1, len(indexSum)):
            a, b = b, max(b, indexSum[i] + a)

        return b

if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn2([2, 2, 3, 3, 3, 4]))