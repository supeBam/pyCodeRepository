import collections
from typing import List, Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        new_len = len(list(set(nums)))
        cnt = collections.Counter()
        # 左指针
        l = 0
        # 移动右指针
        for r, v in enumerate(nums):
            cnt[v] += 1
            # 移动左指针
            while len(cnt) == new_len:
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l += 1
            # 左指针移动的步数为答案
            ans += l
        return ans
