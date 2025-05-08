from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        d = [i for i in range(1, 27)]
        for i, v in enumerate(chars):
            d[ord(v) - 97] = vals[i]

        nums = [0] * n
        for i, v in enumerate(s):
            nums[i] = d[ord(v) - 97]

        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
        return max(dp) if max(dp) > 0 else 0


    # 优化1： 简化
    def maximumCostSubstring2(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        # zip() 按位置 一 一 对应, 长度不同时按最小长度来
        d = dict(zip(chars, vals))
        nums = [d.get(c, ord(c) - 96) for c in s]

        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
        return max(dp) if max(dp) > 0 else 0

if __name__ == '__main__':
    s = Solution()
    # print(s.maximumCostSubstring(s="adaa", chars="d", vals=[-1000]))
    # print(s.maximumCostSubstring(s = "abc", chars = "abc", vals = [-1,-1,-1]))
    print(s.maximumCostSubstring("talaqlt", "tqla", [4, 3, 3, -2]))
