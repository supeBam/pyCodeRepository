class Solution:
    '''
    f(n) 代表 当前地造房子的数量
    一块地的时候 只有 选 和 不选两种
    两块地的时候 dp[0] = 1 dp[1] = 2 dp[2] = 3 dp[3] = 5  dp[4] = 8
    dp[n] = dp[n - 1] + dp[n - 2]
    '''

    def countHousePlacements(self, n: int) -> int:
        mod = 1_000_000_000 + 7
        if n == 1:
            return 4
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod

        return (dp[n] * dp[n]) % mod

    def countHousePlacements2(self, n: int) -> int:
        mod = 1_000_000_000 + 7
        if n == 1:
            return 4
        a = 1
        b = 2
        for i in range(2, n + 1):
            a, b = b, a + b

        return (b * b) % mod


if __name__ == '__main__':
    s = Solution()
    print(s.countHousePlacements2(2))
