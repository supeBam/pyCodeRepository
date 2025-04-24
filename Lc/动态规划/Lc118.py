from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        定义最优结构：f(n,i) = f(n - 1, i) + f(n - 1, i - 1)
        转移方程：dp[n][i] = dp[n - 1][i] + dp[n - 1][i - 1]
        重叠子问题:
        初始状态：f(1) = dp[0][0] = f(2) = dp[1][0] dp[1][1] = 1
        '''
        dp = [[1] * (i + 1) for i in range(numRows)]

        for row in range(2, numRows):
            for col in range(1, row):
                dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))