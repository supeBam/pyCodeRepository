from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        def robRange(start: int, end: int) -> int:
            pre = nums[start]
            cur = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                pre, cur = cur, max(pre + nums[i], cur)
            return cur

        # 如果不选第一间 范围: [1, n - 1]
        ans1 = robRange(1,  n - 1)
        # 选第一间, 范围：[0, n - 2]
        ans2 = robRange(0, n - 2)
        return max(ans1, ans2)
