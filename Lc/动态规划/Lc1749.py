from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp1, dp2 = [0] * n, [0] * n

        ans = 0
        for i in range(n):
            dp1[i] = max(dp1[i - 1], 0) + nums[i]
            dp2[i] = min(dp2[i - 1], 0) + nums[i]
            ans = max(ans, dp1[i], -dp2[i])
        return ans

    # 优化2: 改为变量
    def maxAbsoluteSum2(self, nums: List[int]) -> int:
        ans = max_v = min_v = 0
        for v in nums:
            max_v = max(max_v, 0) + v
            min_v = min(min_v, 0) + v
            ans = max(ans, max_v, -min_v)
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.maxAbsoluteSum([1, -3, 2, 3, -4]))
    # print(s.maxAbsoluteSum([-7, -1, 0, -2, 1, 3, 8, -2, -6, -1, -10, -6, -6, 8, -4, -9, -4, 1, 4, -9]))
    # print(s.maxAbsoluteSum([-10, 12, -31, 8, -17, 5, -9]))
    print(s.maxAbsoluteSum([-1]))
