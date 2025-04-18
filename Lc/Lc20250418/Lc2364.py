
'''
满足条件：
    后面的数一定比前面大
    当出现一个数满足时,相邻的一定相差 1 (找到连续相差1的数组)
'''
from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        # 阶层
        ans = n * (n - 1) // 2
        cnt = Counter()
        for i, x in enumerate(nums):
            ans -= cnt[x - i]
            cnt[x - i] += 1
        return ans
