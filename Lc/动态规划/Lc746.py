from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        最优子结构: min(f(n-1), f(n-2))
        转移方程： f(n) = min(f(n-1), f(n-2))
        存在重叠子结构
        起始位置
        '''

        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[n - 2], dp[n - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs(cost=[10, 15, 20]))
    print(s.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
