class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        '''
        起始状态：f(0) = 1   f(n) 代表 长度为 n 的字符串时 有多少种方案，
        转移方程：f(n) = f(n - z) + f(n - o)
        '''
        dp = [0] * (high + 1)
        dp[0] = 1
        m = 1_000_000_000 + 7

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] = dp[i - zero]
            if i - one >= 0:
                dp[i] = dp[i - one] + dp[i]

        return sum(dp[low:]) % m



