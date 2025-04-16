from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global r
        ans = 0
        count = defaultdict(int)  # 默认值是 0
        l = 0
        # 右指针
        for r in range(len(s)):
            count[s[r]] += 1

            while count[s[r]] >= 2:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans