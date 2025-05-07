from collections import Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        sorted_cnt = sorted(cnt.keys())
        dp = [0] * (len(sorted_cnt) + 1)

        j = 0
        for i, v in enumerate(sorted_cnt):
            while sorted_cnt[j] < v - 2:
                j += 1
            dp[i + 1] = max(dp[i], dp[j] + cnt[v] * v)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.maximumTotalDamage([1, 1, 3, 4]))
    print(s.maximumTotalDamage([7, 1, 6, 6]))
    # print(s.maximumTotalDamage([1, 1, 1, 1, 1, 1]))
