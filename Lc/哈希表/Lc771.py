import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = collections.Counter()
        for stone in stones:
            cnt[stone] += 1

        ans = 0
        for jewel in jewels:
            ans += cnt[jewel]

        return ans