import collections
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        cnt = set()
        while l < r:
            cnt.add((sorted_nums[l] + sorted_nums[r] )/ 2)
            l += 1
            r -= 1

        return len(cnt)
